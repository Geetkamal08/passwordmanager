# Password Manager

This is a minimal in-memory password store built with Flask.

Run the app:

```bash
pip install -r requirements.txt
python app.py
```

Add a username/password (POST):

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"alice","password":"s3cr3t"}' http://localhost:5000/add
```

Get a stored password (GET):

```bash
curl http://localhost:5000/get/alice
```

Notes:

- `POST` for `/add`: POST is required because the request carries a body with data to be stored; GET should be side-effect-free and not include a body.
- Reading JSON in Flask: use `request.get_json()` or access `request.json` to parse the incoming JSON body.
- Error responses: when a username is not found the app returns a `404` with a JSON error message.
- Why test a missing username: to ensure the service correctly handles not-found cases and returns appropriate error codes instead of crashing or returning incorrect data.

