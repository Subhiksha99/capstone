import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app import create_app
from models import setup_db, Movie, Actor





class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        load_dotenv()
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.getenv('TEST_DATABASE_URL')
        
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
			
		

        # Set up authentication tokens info
        with open('auth_config.json', 'r') as f:
            self.auth = json.loads(f.read())

        assistant_jwt = self.auth["roles"]["Casting Assistant"]["jwt_token"]
        director_jwt = self.auth["roles"]["Casting Director"]["jwt_token"]
        producer_jwt = self.auth["roles"]["Casting Producer"]["jwt_token"]
        self.auth_headers = {
            "Casting Assistant": f'Bearer {assistant_jwt}',
            "Casting Director": f'Bearer {director_jwt}',
            "Casting Producer": f'Bearer {producer_jwt}'
        }

        self.movie = {"title": "Good Bad Ugly","release_date": "2025-04-12"}
        self.actor = {
            "name": "Ak",
            "age": 45,
            "gender": 'M',
            "movie_id": 1
        }	
	
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_actors(self):
        header_obj = {"Authorization": self.auth_headers["Casting Assistant"]}
        res = self.client().get("/actors",headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["sucess"], True)
        self.assertTrue(data["actors"])
		
        
    def test_get_actors_permission_not_allowed(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        #self.assertEqual(data["sucess"], False)    
    
    def test_get_movies(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get("/movies",headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["sucess"], True)
        self.assertTrue(data["movies"])
		
        
    def test_get_movies_permission_not_allowed(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        #self.assertEqual(data["sucess"], False)    
    
    def test_create_movie_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().post('/movies', json=self.movie, headers=header_obj)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_create_movie_not_authorise(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().post('/movies', json=self.movie,headers=header_obj)
        self.assertEqual(res.status_code, 401)
		
    def test_create_actor_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().post('/actors', json=self.actor, headers=header_obj)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor'])

    def test_create_actor_not_authorise(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().post('/actors', json=self.actor, headers=header_obj)
        self.assertEqual(res.status_code, 401)
		
    def test_update_movie_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().patch('/movies/2', json={"title": "Updated Title"}, headers=header_obj)
        print(res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['movies']['title'], "Updated Title")

    def test_update_movie_not_found(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().patch('/movies/9999', json={"title": "None"}, headers=header_obj)
        self.assertEqual(res.status_code, 404)
		
    def test_update_actor_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().patch('/actors/1', json={"name": "Updated Name"}, headers=header_obj)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['actors']['name'], "Updated Name")

    def test_update_actor_not_found(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().patch('/actors/9999', json={"name": "None"}, headers=header_obj)
        self.assertEqual(res.status_code, 404)
		
    def test_delete_movie_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().delete('/movies/1', headers=header_obj)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['delete'])

    def test_delete_movie_not_found(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().delete('/movies/9999', headers=header_obj)
        self.assertEqual(res.status_code, 404)
		
    def test_delete_actor_success(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().delete('/actors/4', headers=header_obj)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['delete'])

    def test_delete_actor_not_found(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Producer"]
        }
        res = self.client().delete('/actors/9999', headers=header_obj)
        self.assertEqual(res.status_code, 404)
	


	



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

