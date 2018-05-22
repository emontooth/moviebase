from flask_script import Manager
from moviebase import app, db, Producer, Movie

manager= Manager(app)



@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    christophernolan = Producer(name='Christopher Nolan', about='Christopher Edward Nolan is an English film director, screenwriter, and producer who holds both British and American citizenship. ')
    jamescameron = Producer(name='James Cameron', about='James Francis Cameron (born August 16, 1954) is a Canadian filmmaker, philanthropist, and deep-sea explorer.')
    georgelucas = Producer(name='George Lucas',about = 'George Walton Lucas Jr.[2] (born May 14, 1944) is an American filmmaker and entrepreneur.')
    movie1 = Movie(name='Interstellar', year=2014, actors="Mathew McConaughey", producer=christophernolan)
    movie2 = Movie(name='Avatar', year=2009, actors="Sam Worthington", producer=jamescameron)
    movie3 = Movie(name='Titanic', year=1997, actors="Leonardo DiCaprio", producer=jamescameron)
    movie4 = Movie(name='Star Wars' ,year=1977, actors= "Harrison Ford", producer=georgelucas)
    db.session.add(christophernolan)
    db.session.add(jamescameron)
    db.session.add(georgelucas)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.commit()

if __name__ == '__main__':

        manager.run()
