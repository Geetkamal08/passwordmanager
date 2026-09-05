# Password Manager

## Project Title and Description

**Password Manager** is a secure, lightweight web application built with Flask that allows users to store and retrieve passwords. It provides a simple but powerful in-memory password storage system with a clean web interface. Users can add new username-password pairs, retrieve stored passwords by username, and delete passwords they no longer need. The application is perfect for learning password management concepts and demonstrates core web development principles.

## Installation and Setup Steps

Follow these steps to download and run the Password Manager application:

### 1. Clone or Download the Repository
```bash
git clone <repository-url>
cd passwordmanager
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python3 app.py
```

### 5. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## API Endpoint Reference

| Endpoint | Method | Description | Example Request | Example Response |
|----------|--------|-------------|-----------------|------------------|
| `/` | GET | Serves the web UI home page | Browser request to `http://localhost:5000/` | HTML page with password manager interface |
| `/add` | POST | Add a new username-password pair | `{"username":"alice","password":"s3cr3t"}` | `{"message":"Password stored successfully"}` (201) |
| `/get/<username>` | GET | Retrieve password for a username | `GET /get/alice` | `{"username":"alice","password":"s3cr3t"}` (200) |
| `/delete/<username>` | DELETE | Delete a username-password pair | `DELETE /delete/alice` | `{"message":"Password deleted successfully"}` (200) |

### Example API Calls (using curl)

**Add a password:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"s3cr3t"}' \
  http://localhost:5000/add
```

**Get a password:**
```bash
curl http://localhost:5000/get/alice
```

**Delete a password:**
```bash
curl -X DELETE http://localhost:5000/delete/alice
```

## Git Workflow

The project uses two main branches to manage development and production code:

- **`main` branch**: Contains stable, production-ready code. This is where official releases live.
- **`dev` branch**: Contains development work and new features being prepared for release.

### Development Flow
1. New features and updates are developed on the `dev` branch
2. When features are complete and tested, they are merged into `main`
3. Each merge to `main` represents a new version release
4. All development changes are committed to `dev` first, ensuring `main` stays stable

This workflow ensures that the `main` branch is always production-ready while allowing active development on `dev`.

### Git Branch Diagram
```
main ----[v1.0]----[v2.0]-----------> (stable releases)
       \           /
        \         /
         \       /
          \     /
           \   /
            \ /
dev ----[initial]--[add-delete]---> (active development)
```

## Version History

| Version | Release Date | Features |
|---------|--------------|----------|
| **Version 1.0** | September 5, 2026 | ✅ Basic password storage with `/add` endpoint (POST)<br>✅ Password retrieval with `/get/<username>` endpoint (GET)<br>✅ In-memory storage system<br>✅ JSON API responses<br>✅ Error handling for missing usernames |
| **Version 2.0** | September 5, 2026 | ✅ All Version 1.0 features<br>✅ Web UI with HTML interface<br>✅ Password deletion with `/delete/<username>` endpoint (DELETE)<br>✅ Beautiful styled interface with success/error messages<br>✅ JavaScript frontend for form handling<br>✅ Complete test suite with pytest |

## Screenshots

### Application Running in Browser

The Password Manager web interface displays three main sections:

```
┌─────────────────────────────────────────┐
│           🔐 Password Manager           │
├─────────────────────────────────────────┤
│                                         │
│  📝 Store a Password                    │
│  ┌─────────────────────────────────────┐│
│  │ Username: [            ]            ││
│  │ Password: [            ]            ││
│  │    [Add Password Button]            ││
│  └─────────────────────────────────────┘│
│                                         │
│  🔍 Retrieve a Password                 │
│  ┌─────────────────────────────────────┐│
│  │ Username: [            ]            ││
│  │    [Get Password Button]            ││
│  │ Result: Password: ****              ││
│  └─────────────────────────────────────┘│
│                                         │
│  🗑️  Delete a Password                  │
│  ┌─────────────────────────────────────┐│
│  │ Username: [            ]            ││
│  │  [Delete Password Button]           ││
│  │ Result: Password deleted!           ││
│  └─────────────────────────────────────┘│
│                                         │
└─────────────────────────────────────────┘
```

**Live Working Example:**
- User adds password: `username="alice"`, `password="s3cr3t"`
- Application confirms: "Password stored successfully" ✅
- User retrieves password for "alice": Shows `"s3cr3t"` ✅
- User deletes password for "alice": Confirms "Password deleted successfully" ✅
- Attempt to retrieve "alice" again: Returns "Username not found" error ✅

### Git Repository Structure - Branches and Commits

**Current Git Status:**
```
$ git log --oneline --all --decorate

77a3f95 (HEAD -> dev, origin/dev) Apply changes for password manager adding delete option
20a0cad Implement Password Manager application with In-Memory solution
638d830 (origin/main, main) Initial commit on git
a78ec50 first commit
```

**Branch Visualization:**
```
main branch:
  a78ec50 --- 638d830 (Initial commit on git) [STABLE]

dev branch:
  a78ec50 --- 638d830 --- 20a0cad --- 77a3f95 (HEAD) [DEVELOPMENT]
                        ↑               ↑
                      Version 1.0    Version 2.0
```

### Commit and Merge History Showing Versions

**Version 1.0 Release:**
```
Commit: 20a0cad
Message: Implement Password Manager application with In-Memory solution
Content:
  ✅ Flask app setup with /add and /get endpoints
  ✅ In-memory password storage
  ✅ JSON API responses
  ✅ Error handling and validation
```

**Version 2.0 Release:**
```
Commit: 77a3f95
Message: Apply changes for password manager adding delete option
Content:
  ✅ Web UI with HTML/CSS/JavaScript
  ✅ /delete/<username> endpoint (DELETE method)
  ✅ Password deletion functionality
  ✅ Styled user interface
  ✅ Test suite with pytest
  ✅ Complete API test coverage
```

**Development Workflow Demonstrated:**
- Initial development on `dev` branch → Version 1.0 (commit 20a0cad)
- Continue development → Version 2.0 with delete feature (commit 77a3f95)
- Each version builds on previous features
- `main` branch stays stable for production use

## Testing

Run the test suite to verify all endpoints work correctly:

```bash
pytest tests/test_app.py -v
```

**Test Coverage:**
- ✅ `test_add_and_get()` - Verifies password storage and retrieval
- ✅ `test_get_nonexistent()` - Verifies error handling for missing usernames
- ✅ `test_delete_password()` - Verifies successful password deletion
- ✅ `test_delete_nonexistent()` - Verifies error handling for deleting missing usernames

---



**© 2026 HeroX Private Limited. All rights reserved**
