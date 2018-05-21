from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    #return "<h1> This is not the first page</h1>"
    return render_template('index.html')


@app.route('/users/<string:name>/')
def get_user_name(name):
    return render_template('users.html')


if __name__ == '__main__':

        app.run(debug=True)
