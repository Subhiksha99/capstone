Casting Agency Project

Udacity nanodegree fullstack project.

Deployed url: "https://capstone-4r5f.onrender.com/"

🎬 Project Motivation – Casting Agency App

In the modern entertainment industry, efficient talent and project management is vital for success. Casting directors and production managers often struggle with organizing actors, managing their assignments, and tracking film projects — especially when dealing with multiple roles, permissions, and updates across teams.

This Casting Agency application was developed to address those pain points by providing:

🎭 A centralized platform to manage actors and movies efficiently.

🔐 Role-based access control, ensuring producers, casting assistants, and directors access only what they need.

🛠️ RESTful APIs for creating, updating, and deleting actor/movie records, making integration with front-end tools or mobile apps seamless.

📋 Error handling and validation, improving robustness and user experience.

The project also serves as a real-world demonstration of secure API design using:

Flask and SQLAlchemy for scalable backend development.

Auth0 for role-based authentication and authorization.

PostgreSQL for relational data modeling.

Automated testing for ensuring API reliability.

This project not only strengthens backend engineering skills but also aligns with industry needs for building secure, scalable applications — essential for modern media organizations managing talent and content production workflows.

🧰 Tech Stack & Tools Used

🖥️ Backend Technologies

Python 3.9+
Core programming language used to build the application.

Flask
A lightweight web framework used to create RESTful APIs.

Flask-CORS
Handles Cross-Origin Resource Sharing, allowing the API to interact with a frontend hosted on a different domain.

Flask-Migrate
Manages SQLAlchemy database migrations using Alembic.

Flask-SQLAlchemy
ORM (Object Relational Mapper) used to interact with the PostgreSQL database in an object-oriented way.

SQLAlchemy
Core ORM library for database operations.

🛠️ Database

PostgreSQL
A robust, open-source relational database used to store actors, movies, and relationships between them.

🔐 Authentication & Authorization

Auth0
Provides OAuth2-based identity management. Used to:

Secure endpoints using JSON Web Tokens (JWT).

Implement role-based access control (RBAC) for different user roles (e.g., Casting Assistant, Director, Executive Producer).

python-jose
Library used for decoding and validating JWTs issued by Auth0.

🧪 Testing & Validation

unittest (Python built-in)
Framework used for writing test cases to validate success and failure scenarios for each API endpoint.

Postman
Useful during development to manually test endpoints with different roles and tokens.

☁️ Deployment

Render
Cloud platform used for deploying the Flask backend. Automatically installs dependencies, sets environment variables, and runs the app.

📦 Environment Management

pip
Used to install dependencies listed in requirements.txt.

python-dotenv
Loads environment variables from a .env file (useful for local development).

Project setup in Local

Create a virtual environment

python -m venv myenv

cd myenv/Scripts

activate.bat

Install required dependency Library

pip install -r requirements.txt

setup a database

psql -U postgres -f database_setup.sql


To run an application

if you are using windows, use "set" command

set FLASK_APP= app.py

if you are using Linus , use "export" command

export FLASK_APP= app.py

flask run --reload

To run a test file

psql -U postgres -f test_database_setup.sql

python test_flaskr.py


🔐 Auth0 Setup Guide

To enable secure authentication and role-based access in your Casting Agency project, follow the steps below to configure Auth0.

✅ Step 1: Create an Auth0 Account

Go to Auth0 and sign up or log in to create your tenant.

⚙️ Step 2: Configure Environment Variables (setup.sh)

Define the following variables in your setup.sh file:

export AUTH0_DOMAIN="your-tenant.auth0.com"     # Your Auth0 domain

export ALGORITHMS="RS256"                        # Signing algorithm

export API_AUDIENCE="capstone"                   # API identifier set in Auth0


👤 Step 3: Create Roles

Navigate to User Management > Roles in the Auth0 dashboard and create these three roles:

Casting Assistant

Permissions: View actors and movies

Casting Director

Inherits all Casting Assistant permissions

Can add, delete, and modify actors

Can modify movies

Executive Producer

Inherits all Casting Director permissions

Can add and delete movies

🔑 Step 4: Set API Permissions

Under your created API in Auth0, add the following permissions:

get:actors

get:movies

post:actors

patch:actors

delete:actors

post:movies

patch:movies

delete:movies

🧪 Step 5: Generate JWT Tokens (auth_config.json)

You can create users and log them in via the following URL format to generate access tokens:

https://<YOUR_DOMAIN>/authorize?
  audience=<API_IDENTIFIER>&
  response_type=token&
  client_id=<YOUR_CLIENT_ID>&
  redirect_uri=<YOUR_CALLBACK_URI>

Replace placeholders with values from your Auth0 dashboard.


Endpoints
Movies
1. GET /movies
Description: Fetches all movies.

Permissions required: get:movies

Request:
GET /movies

Response:
{
  "success": true,
  "movies": [
    {
      "id": 1,
      "title": "Movie Title",
      "release_date": "2025-01-01",
      "actors": []
    }
  ]
}
2. POST /movies
Description: Create a new movie.

Permissions required: post:movies

Request:

{
  "title": "New Movie",
  "release_date": "2025-05-01"
}
Response:
{
  "success": true,
  "movies": [
    {
      "id": 2,
      "title": "New Movie",
      "release_date": "2025-05-01",
      "actors": []
    }
  ]
}
3. PATCH /movies/<movie_id>
Description: Update an existing movie.

Permissions required: patch:movies

Request:

{
  "title": "Updated Title",
  "release_date": "2025-06-01"
}
Response:

{
  "success": true,
  "movies": {
    "id": 1,
    "title": "Updated Title",
    "release_date": "2025-06-01",
    "actors": []
  }
}
4. DELETE /movies/<movie_id>
Description: Delete a movie by ID.

Permissions required: delete:movies

Request:
DELETE /movies/1

Response:

{
  "success": true,
  "delete": 1
}

Actors
1. GET /actors
Description: Fetch all actors.

Permissions required: get:actors

Request:
GET /actors

Response:

{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "Actor Name",
      "age": 30,
      "gender": "Male",
      "movie_id": 1
    }
  ]
}
2. POST /actors
Description: Create a new actor.

Permissions required: post:actors

Request:

{
  "name": "New Actor",
  "age": 28,
  "gender": "Female",
  "movie_id": 1
}
Response:

{
  "success": true,
  "actor": [
    {
      "id": 2,
      "name": "New Actor",
      "age": 28,
      "gender": "Female",
      "movie_id": 1
    }
  ]
}
3. PATCH /actors/<actor_id>
Description: Update an actor's details.

Permissions required: patch:actors

Request:

{
  "name": "Updated Actor",
  "age": 35,
  "gender": "Male"
}
Response:

{
  "success": true,
  "drinks": {
    "id": 1,
    "name": "Updated Actor",
    "age": 35,
    "gender": "Male",
    "movie_id": 1
  }
}
4. DELETE /actors/<actor_id>
Description: Delete an actor by ID.

Permissions required: delete:actors

Request:
DELETE /actors/1

Response:

{
  "success": true,
  "delete": 1
}
⚠️ Error Handling

Error Code	Meaning
400	Bad Request (malformed request)

401	Unauthorized (token missing/invalid)

404	Resource Not Found

422	Unprocessable Entity

500	Internal Server Error