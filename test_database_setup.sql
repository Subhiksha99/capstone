DROP DATABASE IF EXISTS capstone_test;

CREATE DATABASE capstone_test;

\c capstone_test;

-- Drop tables if they already exist
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS movies;

-- Create the movies table
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    release_date TIMESTAMP
);

-- Create the actors table
CREATE TABLE actors (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    age INTEGER,
    gender VARCHAR,
    movie_id INTEGER REFERENCES movies(id)
);

-- Insert dummy data into movies
INSERT INTO movies (title, release_date) VALUES 
('Inception', '2010-07-16'),
('Interstellar', '2014-11-07'),
('The Matrix', '1999-03-31');

-- Insert dummy data into actors
INSERT INTO actors (name, age, gender, movie_id) VALUES 
('Leonardo DiCaprio', 45, 'Male', 1),
('Joseph Gordon-Levitt', 39, 'Male', 1),
('Matthew McConaughey', 50, 'Male', 2),
('Anne Hathaway', 38, 'Female', 2),
('Keanu Reeves', 55, 'Male', 3),
('Carrie-Anne Moss', 52, 'Female', 3);
