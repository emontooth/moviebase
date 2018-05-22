import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Producer(db.Model):
    __tablename__ = 'Producers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    movies = db.relationship('Movie', backref='producer', cascade="delete")



class Movie(db.Model):
    __tablename__ = 'Movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    actors = db.Column(db.Text)
    producer_id = db.Column(db.Integer, db.ForeignKey('Producers.id'))

@app.route('/')
def homepage():
    #return "<h1> This is not the first page</h1>"
    return render_template('homepage.html')


@app.route('/producers')
def show_all_producers():
        producers = Producer.query.all()
        return render_template('producer-all.html', producers=producers)



@app.route('/producer/add', methods=['GET', 'POST'])
def add_producers():
    if request.method == 'GET':
        return render_template('producer-add.html')
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']

        producer = Producer(name=name, about=about)
        db.session.add(producer)
        db.session.commit()
        return redirect(url_for('show_all_producers'))


@app.route('/api/producer/add', methods=['POST'])
def add_ajax_producers():
    name = request.form['name']
    about = request.form['about']

    producer = Producer(name=name, about=about)
    db.session.add(producer)
    db.session.commit()

    flash('Producer Inserted', 'success')
    return jsonify({"id": str(producer.id), "name": producer.name})



@app.route('/producer/edit/<int:id>', methods=['GET', 'POST'])
def edit_producer(id):
    producer = Producer.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('producer-edit.html', producer=producer)
    if request.method == 'POST':
        producer.name = request.form['name']
        producer.about = request.form['about']
        db.session.commit()
        return redirect(url_for('show_all_producers'))




@app.route('/producer/delete/<int:id>', methods=['GET', 'POST'])
def delete_producer(id):
    producer = Producer.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('producer-delete.html', producer=producer)

    if request.method == 'POST':
        producer.query.filter_by(id=id).delete()
        db.session.delete(producer)
        db.session.commit()
        return redirect(url_for('show_all_producers'))


@app.route('/api/producer/<int:id>', methods=['DELETE'])
def delete_ajax_producer(id):
    producer = Producer.query.get_or_404(id)
    db.session.delete(producer)
    db.session.commit()
    return jsonify({"id": str(producer.id), "name": producer.name})


@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)



@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        producers = Producer.query.all()
        return render_template('movie-add.html', producers=producers)

    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        actors = request.form['actors']
        producer_name = request.form['producer']
        producer = Producer.query.filter_by(name=producer_name).first()
        movie = Movie(name=name, year=year, actors=actors, producer=producer)
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('show_all_movies'))



@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    producers = Movie.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, producers=producers)
    if request.method == 'POST':
        movie.name = request.form['name']
        movie.year = request.form['year']
        movie.actors = request.form['actors']
        producer_name = request.form['producer']
        producer = Producer.query.filter_by(name=producer_name).first()
        movie.producer = producer
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))



@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    producers = Producer.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, producers=producers)
    if request.method == 'POST':
        # use the id to delete the song
        movie.query.filter_by(id=id).delete()
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})




@app.route('/users')
def show_all_users():
    return render_template('user-all.html')


@app.route('/users/<string:name>/')
def get_user_name(name):
    return render_template('users.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/movie/<int:id>/')
def get_movie_id(id):
    return "Hi, this is %s and the movie's id is %d" % ('administrator', id)




if __name__ == '__main__':

        app.run(debug=True)
