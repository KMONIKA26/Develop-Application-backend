# Develop-Application-backend


# Blogging Platform API

## Overview

This is a REST API for a blogging platform with user authentication and role-based access control. The platform allows users to register, log in, create posts, and comment on posts. The API is built using Flask, SQLAlchemy, and PostgreSQL.

## Features

- **User Registration & Login**: Users can register and log in to access the platform.
- **Role-Based Access Control**: Different roles ("admin", "author", "reader") with varying levels of access.
- **Post Management**: Authenticated users with appropriate roles can create and manage blog posts.
- **Commenting System**: Users can comment on blog posts.
- **Pagination**: Supports pagination for retrieving posts.

## Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/blogging-platform-api.git
   cd blogging-platform-api
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL:**

   Create a PostgreSQL database named `blog_platform`.

   ```sql
   CREATE DATABASE blog_platform;
   ```

4. **Configure the Database:**

   Update the database connection string in `config.py`:

   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/blog_platform'
   ```

5. **Run Database Migrations:**

   Initialize the database tables:

   ```bash
   flask db upgrade
   ```

6. **Run the application:**

   ```bash
   python app.py
   ```

   The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. User Registration & Login

- **Register**: `POST /api/register`
  - Requires `username`, `email`, and `password`.
  - Hashes the password before storing it in the database.

- **Login**: `POST /api/login`
  - Requires `username` and `password`.
  - Returns a JWT token upon successful authentication.

### 2. Create a Post

- **Endpoint**: `POST /api/posts`
- **Description**: Allows an authenticated user with the role of "author" or "admin" to create a post.
- **Headers**: Requires JWT token for authentication.
- **Request Body**:

  ```json
  {
      "title": "My First Post",
      "content": "This is the content of my first post."
  }
  ```

### 3. Get All Posts

- **Endpoint**: `GET /api/posts`
- **Description**: Retrieves a list of all posts, optionally filtered by author using a query parameter (`?author=username`).
- **Pagination**: Implemented with a page size of 2 posts per page.

### 4. Add Comment to a Post

- **Endpoint**: `POST /api/posts/{post_id}/comments`
- **Description**: Allows an authenticated user to comment on a post.
- **Headers**: Requires JWT token for authentication.
- **Request Body**:

  ```json
  {
      "content": "Great post!"
  }
  ```

## Testing

You can use **Postman** or **curl** to test the API endpoints.

### Example curl commands:

1. **User Registration:**

   ```bash
   curl -X POST \
     http://127.0.0.1:5000/api/register \
     -H 'Content-Type: application/json' \
     -d '{"username": "johndoe", "email": "john@example.com", "password": "securepassword"}'
   ```

2. **User Login:**

   ```bash
   curl -X POST \
     http://127.0.0.1:5000/api/login \
     -H 'Content-Type: application/json' \
     -d '{"username": "johndoe", "password": "securepassword"}'
   ```

3. **Create a Post:**

   ```bash
   curl -X POST \
     http://127.0.0.1:5000/api/posts \
     -H 'Authorization: Bearer YOUR_JWT_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{"title": "My First Post", "content": "This is the content of my first post."}'
   ```

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# Expense Management System

## Overview

This is a simple REST API for managing user expenses across different bank accounts. The system is built using Flask, MongoDB, and PyMongo. It allows users to add and track expenses associated with their bank accounts.

## Features

- **User Management**: Manage users who have multiple bank accounts.
- **Expense Tracking**: Track expenses per account for each user.
- **NoSQL Database**: MongoDB is used to store users, accounts, and expenses.

## Prerequisites

- Python 3.x
- MongoDB
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**

   Make sure MongoDB is running locally on `mongodb://localhost:27017/expense_manager`.

4. **Configuration:**

   You can configure the MongoDB connection string in `config.py`.

   ```python
   MONGO_URI = 'mongodb://localhost:27017/expense_manager'
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

   The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Add an Expense to an Account

- **Endpoint**: `POST /api/users/{user_id}/accounts/{account_id}/expenses`
- **Description**: Adds a new expense to a specified account for a user.

#### Request Body

```json
{
    "description": "Groceries",
    "amount": 50
}
```

#### Response

```json
{
    "message": "Expense added successfully",
    "expense": {
        "_id": "64edbd1f3c2a7c0c7d7d",
        "description": "Groceries",
        "amount": 50,
        "date": "2024-09-03"
    }
}
```

### 2. Get All Expenses for a User Account

- **Endpoint**: `GET /api/users/{user_id}/accounts/{account_id}/expenses`
- **Description**: Retrieves all expenses for a specified account of a user.

#### Response

```json
{
    "account": "64edbd1f3c2a7c0c7d7d",
    "expenses": [
        {
            "_id": "64edbd1f3c2a7c0c7d7e",
            "description": "Groceries",
            "amount": 50,
            "date": "2024-09-03"
        }
    ]
}
```

## Testing

You can use **Postman** or **curl** to test the API endpoints.

### Example curl commands:

1. **Add an Expense:**

   ```bash
   curl -X POST \
     http://127.0.0.1:5000/api/users/{user_id}/accounts/{account_id}/expenses \
     -H 'Content-Type: application/json' \
     -d '{"description": "Dinner", "amount": 30}'
   ```

2. **Get All Expenses:**

   ```bash
   curl -X GET \
     http://127.0.0.1:5000/api/users/{user_id}/accounts/{account_id}/expenses
   ```

## API Documentation
For detailed API documentation, refer to the following Postman links:
- [Blogging Platform API Documentation](https://documenter.getpostman.com/view/26079619/2sA3duHDrm)
- [Expense Management System API Documentation](https://documenter.getpostman.com/view/8091590/2s8YRnmXTd)


## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
