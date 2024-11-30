# CSC207 Project Server

A simple webserver for my [CSC207 Project](https://github.com/ChristopherLi05/CSC207-Project)

# API Specifications

1. [User Signup](#1-user-signup)
2. [User Login](#2-user-login)
3. [Leaderboard](#3-leaderboard)
4. [Update Score](#4-update-score)
5. [Best Score](#5-best-score)

## 1. User Signup
**Endpoint:**
`POST /api/v1/signup`

**Description:**
Allows a new user to create an account by providing a username and password.

**Request Format:**

Content-Type: `application/json`
Body:
```
{
    "username": "string",
    "password": "string"
}
```
**Response Format:**

**Success (200 OK):**
```
{
    "success": true
}
```

**Error:**
* 400 Bad Request: Missing request body.
```
{
    "success": false,
    "error": "Did not specify  body"
}
```

* 403 Forbidden: Username or password not provided.
```
{
    "success": false,
    "error": "Username field not present"
}
```

```
{
    "success": false,
    "error": "Password field not present"
}
```

* 403 Forbidden: Invalid username or password.
```
{
    "success": false,
    "error": "Username is not valid"
}
```

```
{
    "success": false,
    "error": "Password is not valid"
}
```

* 403 Forbidden: Username already exists.
```
{
    "success": false,
    "error": "Username already exists"
}
```

**Validation Rules:**
* username: Must be 3–16 alphanumeric characters.
* password: Must be 5–20 characters long.

## 2. User Login
**Endpoint:**
`POST /api/v1/login`

**Description:**
Authenticates a user with their username and password.

**Request Format:**
Content-Type: `application/json`
Body:
```
{
    "username": "string",
    "password": "string"
}
```

**Response Format:**

**Success (200 OK):**
```
{
    "success": true,
    "session_id": "string"
}
```

**Error:**

* 400 Bad Request: Missing request body.
```
{
    "success": false,
    "error": "Did not specify json body"
}
```

* 403 Forbidden: Username or password not provided.
```
{
    "success": false,
    "error": "username field not present"
}
```
```
{
    "success": false,
    "error": "password field not present"
}
```

* 401 Unauthorized: Username and password do not match.
```
{
    "success": false,
    "error": "Username and Password do not match"
}
```

## 3. Leaderboard
**Endpoint:**
`GET /api/v1/leaderboard`

**Description:**
Retrieves the top 10 scores from the leaderboard.

**Request Format:**
No parameters required.

**Response Format:**

**Success (200 OK):**
```
{
    "success": true,
    "leaderboard": [
        {"username": "string", "score": int},
        ...
    ]
}
```

## 4. Update Score
**Endpoint:**
`POST /api/v1/update_score`

**Description:**
Updates the user's score if the new score is higher than the current best.

**Request Format:**
Content-Type: `application/json`
Body:
```
{
    "session_id": "string",
    "score": int
}
```

**Response Format:**

**Success (200 OK):**
```
{
    "success": true,
    "best_score": int
}
```

**Error:**
* 400 Bad Request: Missing request body.
```
{
    "success": false,
    "error": "Did not specify json body"
}
```

* 403 Forbidden: Missing or invalid fields.
```
{
    "success": false,
    "error": "session_id id field not present"
}
```
```
{
    "success": false,
    "error": "score field not present"
}
```
```
{
    "success": false,
    "error": "score field is not an integer"
}
```
* 403 Forbidden: Invalid or expired session.
```
{
    "success": false,
    "error": "There are no active sessions associated with session_id"
}
```
Validation Rules:
* score: Must be an integer.
* session_id: Must correspond to an active session.

## 5. Best Score
**Endpoint:**
`POST /api/v1/best_score`

**Description:**
Retrieves the best score of the user associated with the session ID.

**Request Format:**
Content-Type: `application/json`
Body:
```
{
    "session_id": "string"
}
```

**Response Format:**

**Success (200 OK):**
```
{
    "success": true,
    "best_score": int
}
```

**Error:**
* 400 Bad Request: Missing request body.
```
{
    "success": false,
    "error": "Did not specify json body"
}
```
* 403 Forbidden: Missing or invalid session ID.
```
{
    "success": false,
    "error": "session_id id field not present"
}
```
* 403 Forbidden: Invalid or expired session.
```
{
    "success": false,
    "error": "There are no active sessions associated with session_id"
}
```
