Casting Agency Project
Developed endpoints for performing CURD operation for movies and actors data model
Deployed url: ""

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
set FLASK_APP= app.py
flask run --reload

To run a test file
psql -U postgres -f test_database_setup.sql
python test_flaskr.py


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