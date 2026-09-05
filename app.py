from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory store for username -> password
store = {}

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Password Manager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .section {
            margin: 30px 0;
            padding: 20px;
            background: #f9f9f9;
            border-left: 4px solid #007bff;
            border-radius: 4px;
        }
        .section h2 {
            margin-top: 0;
            color: #007bff;
            font-size: 1.2em;
        }
        input, button {
            padding: 10px;
            margin: 8px 0;
            width: 100%;
            box-sizing: border-box;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 15px;
            padding: 12px;
            border-radius: 4px;
            display: none;
        }
        .success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 Password Manager</h1>

        <div class="section">
            <h2>Store a Password</h2>
            <input type="text" id="addUsername" placeholder="Username">
            <input type="password" id="addPassword" placeholder="Password">
            <button onclick="addPassword()">Add Password</button>
            <div id="addResult" class="result"></div>
        </div>

        <div class="section">
            <h2>Retrieve a Password</h2>
            <input type="text" id="getUsername" placeholder="Username">
            <button onclick="getPassword()">Get Password</button>
            <div id="getResult" class="result"></div>
        </div>

        <div class="section">
            <h2>Delete a Password</h2>
            <input type="text" id="deleteUsername" placeholder="Username">
            <button onclick="deletePassword()">Delete Password</button>
            <div id="deleteResult" class="result"></div>
        </div>
    </div>

    <script>
        function addPassword() {
            const username = document.getElementById('addUsername').value;
            const password = document.getElementById('addPassword').value;
            const resultDiv = document.getElementById('addResult');

            if (!username || !password) {
                showResult(resultDiv, 'Both username and password are required', false);
                return;
            }

            fetch('/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            })
            .then(res => res.json())
            .then(data => {
                showResult(resultDiv, data.message || data.error, !data.error);
                if (!data.error) {
                    document.getElementById('addUsername').value = '';
                    document.getElementById('addPassword').value = '';
                }
            })
            .catch(err => showResult(resultDiv, 'Error: ' + err, false));
        }

        function getPassword() {
            const username = document.getElementById('getUsername').value;
            const resultDiv = document.getElementById('getResult');

            if (!username) {
                showResult(resultDiv, 'Please enter a username', false);
                return;
            }

            fetch('/get/' + encodeURIComponent(username))
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    showResult(resultDiv, data.error, false);
                } else {
                    showResult(resultDiv, 'Password: ' + data.password, true);
                }
            })
            .catch(err => showResult(resultDiv, 'Error: ' + err, false));
        }

        function deletePassword() {
            const username = document.getElementById('deleteUsername').value;
            const resultDiv = document.getElementById('deleteResult');

            if (!username) {
                showResult(resultDiv, 'Please enter a username', false);
                return;
            }

            fetch('/delete/' + encodeURIComponent(username), {
                method: 'DELETE'
            })
            .then(res => res.json())
            .then(data => {
                showResult(resultDiv, data.message || data.error, !data.error);
                if (!data.error) {
                    document.getElementById('deleteUsername').value = '';
                }
            })
            .catch(err => showResult(resultDiv, 'Error: ' + err, false));
        }

        function showResult(element, message, isSuccess) {
            element.textContent = message;
            element.className = 'result ' + (isSuccess ? 'success' : 'error');
            element.style.display = 'block';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/add', methods=['POST'])
def add():
    if not request.is_json:
        return jsonify({'error': 'Expected JSON body'}), 400
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Both username and password are required'}), 400
    store[username] = password
    return jsonify({'message': 'Password stored successfully'}), 201

@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    if username not in store:
        return jsonify({'error': 'Username not found'}), 404
    return jsonify({'username': username, 'password': store[username]}), 200

@app.route('/delete/<username>', methods=['DELETE'])
def delete_password(username):
    if username not in store:
        return jsonify({'error': 'Username not found'}), 404
    del store[username]
    return jsonify({'message': 'Password deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
