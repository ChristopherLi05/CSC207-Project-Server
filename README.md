# CSC207 Project Server

A simple webserver for my [CSC207 Project](https://github.com/ChristopherLi05/CSC207-Project)

# API Specifications

## 1. User Signup
**Endpoint:**
`POST /api/v1/signup`

**Description:**
Allows a new user to create an account by providing a username and password.

**Request Format:**

Content-Type: `application/json`
Body:
```json
{
    "username": "string",
    "password": "string"
}
```
**Response Format:**

**Success (200 OK):**
```json
{
    "success": true
}
```

**Error:**
* 400 Bad Request: Missing request body.
```json
{
    "success": false,
    "error": "Did not specify json body"
}
```

* 403 Forbidden: Username or password not provided.
```json
{
    "success": false,
    "error": "Username field not present"
}
```

```json
{
    "success": false,
    "error": "Password field not present"
}
```

* 403 Forbidden: Invalid username or password.
```json
{
    "success": false,
    "error": "Username is not valid"
}
```

```json
{
    "success": false,
    "error": "Password is not valid"
}
```

* 403 Forbidden: Username already exists.
```json
{
    "success": false,
    "error": "Username already exists"
}
```

**Validation Rules:**
username: Must be 3–16 alphanumeric characters.
password: Must be 5–20 characters long.

## 2. User Login
**Endpoint:**
`POST /api/v1/login`

**Description:**
Authenticates a user with their username and password.

**Request Format:**
Content-Type: `application/json`
Body:
```json
{
    "username": "string",
    "password": "string"
}
```

**Response Format:**

**Success (200 OK):**
```json
{
    "success": true,
    "session_id": "string"
}
```

**Error:**

* 400 Bad Request: Missing request body.
```json
{
    "success": false,
    "error": "Did not specify json body"
}
```

* 403 Forbidden: Username or password not provided.
```json
{
    "success": false,
    "error": "username field not present"
}
```
```json
{
    "success": false,
    "error": "password field not present"
}
```

* 401 Unauthorized: Username and password do not match.
```json
{
    "success": false,
    "error": "Username and Password do not match"
}```
