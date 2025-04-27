import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from models import setup_db,Movie,Actor
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/movies',methods =['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.all()
        movies = list(map(lambda movie: movie.format(), movies))

        return jsonify({
            'sucess': True,
            'movies': movies
            })

    
    @app.route('/actors',methods = ["GET"])
    @requires_auth('get:actors')
    def get_actors(jwt):
        actors= Actor.query.all()

        return jsonify({
            'sucess':True,
            'actors':[actor.format() for actor in actors]
            })

# to create a movie title and relese date is needed
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        data = request.get_json()
        print(data)
        if data is None:
            abort(400)
            
        title = data.get('title')
        release_date = data.get('release_date')
    
        if not title or release_date is None:
            abort(422)

        
        movie = Movie(title=title, release_date=release_date)

        movie.insert()

        return jsonify({
            'success': True,
            'movies': [movie.format()]
        })
# to create a actor, name, age and gender is needed
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(jwt):
        data = request.get_json()
        print("data",data)
        if data is None:
            abort(400)
            
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        movie_id = data.get('movie_id')
        
        if not name or age is None or not gender  or movie_id is None:
            abort(422)

        
        actor = Actor(name=name,age=age,gender=gender, movie_id = movie_id)
        print("coming after actor")
        actor.insert()

        return jsonify({
            'success': True,
            'actor': [actor.format()]
        })



    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):
        updated_movie = Movie.query.get(movie_id)
        if updated_movie is None:
            abort(404)

        data = request.get_json()
        print(data)
        if 'title' in data:
            updated_movie.title = data['title']

        if 'release_date' in data:
            updated_movie.release_date = data['release_date']

        updated_movie.update()

        return jsonify({
            'success': True,
            'movies': updated_movie.format()
        })
    
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)

        data = request.get_json()
        if 'name' in data:
            actor.name = data['name']

        if 'age' in data:
            actor.age = data['age']
            
        if 'gender' in data:
            actor.gender = data['gender']
            
        if 'movie_id' in data:
            actor.movie_id = data['movie_id']
            
            

        actor.update()

        return jsonify({
            'success': True,
            'actors': actor.format()
        })


    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def remove_movie(jwt, movie_id):

        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'delete': movie.id
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def remove_actor(jwt, actor_id):

        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'delete': actor.id
        })




    # Error Handling
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


   
    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    
    @app.errorhandler(401)
    def unauthorise(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorised"
        }), 401

    @app.errorhandler(AuthError)
    def process_AuthError(error):
        response = jsonify(error.error)
        response.status_code = error.status_code

        return response



    return app

app = create_app()

if __name__ == '__main__':
    app.run()
