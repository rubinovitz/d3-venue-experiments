from flask import Flask
import os
from flask import render_template
from flask import Flask
from werkzeug import SharedDataMiddleware
import os

app = Flask(__name__)

@app.route('/2')
def indextwo():
	return render_template('page2.html')



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/3')
def three():
	return render_template('page3.html');

# store static files on server for now
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
'/': os.path.join(os.path.dirname(__file__), 'static')
})


if __name__ == '__main__':
    app.run(port=3000)
