from flask import Flask, jsonify, request
import csv

movieslist = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    movieslist = data[1:]

likedmovies = []
dislikedmovies = []
notwatchedmovies = []

app = Flask(__name__)

@app.route("/getmovies")
def getmovies():
    return jsonify({
        "data": movieslist[0],
        "status": "success"
    })

@app.route("/likedmovies", method = ["POST"])
def likedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    likedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/dislikedmovies", method = ["POST"])
def dislikedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    dislikedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/notwatchedmovies", method = ["POST"])
def notwatchedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    notwatchedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()