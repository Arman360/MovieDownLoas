from flask import render_template
from app import app
from app.models import Movie, TVShow

@app.route('/')
@app.route('/index')
def index():
    movies = Movie.query.order_by(Movie.rank).all()
    tv_shows = TVShow.query.order_by(TVShow.rank).all()
    return render_template('index.html', movies=movies, tv_shows=tv_shows)

@app.route('/movie/<int:id>')
def movie_detail(id):
    movie = Movie.query.get_or_404(id)
    return render_template('movie_detail.html', movie=movie)

@app.route('/tv_show/<int:id>')
def tv_show_detail(id):
    tv_show = TVShow.query.get_or_404(id)
    return render_template('tv_show_detail.html', tv_show=tv_show)
