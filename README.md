
# Profile Creation System

This is a Django-based API for creating student profiles. It validates user input, enforces password policies, and stores profile data in a PostgreSQL database.

The project is implemented using Django and Django REST Framework (DRF), with PostgreSQL as the backend database.


## Installation and Setup

1. Clone the repository: 'https://github.com/afeef-c/-Profile-Creation-System-Api.git'
    git clone https://github.com/afeef-c/-Profile-Creation-System-Api.git cd <repository-folder>


2. Set up a virtual environment:
    python -m venv env source env/bin/activate ( On Windows: env\Scripts\activate)

3. Install dependencies:
    pip install -r requirements.txt


4. Set up the database:
    - Install PostgreSQL if not already installed.
    - Create a new database (e.g., `profile_system`).
    - Update the `DATABASES` setting in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'profile_system',
            'USER': 'your_postgres_user',
            'PASSWORD': 'your_postgres_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Apply migrations:
    python manage.py makemigrations, python manage.py migrate


6. Run the server:
    python manage.py ruserver


The server will be available at `http://127.0.0.1:8000/`.






# Profile Creation System

## API Endpoints

### 1. Create Student Profile
**Endpoint:** `/api/create-profile/`  
**Method:** `POST`  
**Description:** Creates a new student profile.

#### Request Body:
```json
{
    "name": "John Doe",          // Required (String)
    "email": "john@example.com", // Required (Valid Email)
    "password": "Password123!",  // Required (Password meeting policy)
    "phone": "1234567890"        // Optional (Numeric)
}

Response:
Success (201 Created):

{
    "message": "Profile created successfully!",
    "data": {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    }
}

Validation Error (400 Bad Request):

{
    "errors": {
        "password": [
            "Password must be at least 8 characters long.",
            "Password must contain at least one uppercase letter."
        ]
    }
}