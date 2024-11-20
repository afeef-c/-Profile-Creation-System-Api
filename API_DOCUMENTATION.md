# API Documentation - Profile Creation System

This document provides detailed information about the API endpoints for the **Profile Creation System**. The system allows users to create student profiles and validates passwords against specified policies.

---

## 1. Create Student Profile

**Endpoint:** `/api/create-profile/`  
**Method:** `POST`  
**Description:** The request body must contain the following fields:

    - name: (Required, String) The student's full name.
    - email: (Required, String) A valid email address.
    - password: (Required, String) The password for the student profile.
            Password must meet the following criteria:
            At least 8 characters long.
            Contains at least one uppercase letter (A-Z).
            Contains at least one lowercase letter (a-z).
            Includes at least one numeric digit (0-9).
            Includes at least one special character (e.g., @, #, $, %, etc.).
    - phone : (Optional, Numeric) The student's phone number..

### Request Body:
```json
{
    "name": "John Doe",          // Required (String)
    "email": "john@example.com", // Required (Valid Email)
    "password": "Password123!",  // Required (Password meeting policy)
    "phone": "1234567890"        // Optional (Numeric)
}

###Response:
**Success (201 Created): If the profile is created successfully, the system will respond with the following:**

```json
{
    "message": "Profile created successfully!",
    "data": {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    }
}

**Error (400 Bad Request): If the provided data is invalid (e.g., password doesn't meet policy requirements), the system will return the following validation errors:**

```json
{
    "errors": {
        "password": [
            "Password must be at least 8 characters long.",
            "Password must contain at least one uppercase letter."
        ]
    }
}



## Running Unit Tests
    **Make sure your virtual environment is active and the database is set up.**
    **Run the tests:**
```json
    run the code python manage.py test

