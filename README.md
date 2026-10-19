# Book Tracker API

A robust, secure backend API built for tracking books, managing user reading lists, and handling user authentication. Built with FastAPI, SQLAlchemy, and PostgreSQL.

---

## Features

* **User Authentication:** Secure user registration and login using JWT (JSON Web Tokens) and password hashing (Passlib/Bcrypt).
* **Book Management (CRUD):** Create, read, update, and delete book entries tied to specific users.
* **Database Integration:** Utilizes SQLAlchemy ORM with PostgreSQL for persistent relational data storage.
* **Data Validation:** Powered by Pydantic models to ensure clean input validation and robust API responses.
* **Interactive API Documentation:** Automatically generated Swagger UI and ReDoc endpoints.

---

## Tech Stack

* **Language:** Python 3.9+
* **Framework:** FastAPI
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **Authentication:** python-jose (JWT), Passlib
* **Server:** Uvicorn

---

## Getting Started Locally

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

* Python 3.9 or higher installed on your machine.
* PostgreSQL installed and running locally.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/book-tracker-api.git](https://github.com/your-username/book-tracker-api.git)
   cd book-tracker-api

2. **Create and activate a virtual environment:**
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependdencies:**
    pip install -r requirements.txt

4. **Set up your environment variables:**
    Create a .env file in the root directory of the project and add the following keys:

5. **Run the development server:** 
    uvicorn main:app --reload

6. **Access the API:**
Open your browser and navigate to http://127.0.0.1:8000/docs to test the endpoints via the interactive Swagger UI.