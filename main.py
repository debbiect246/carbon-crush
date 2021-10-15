from replit import web
import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.render_template('index.html')

@app.route('/info/')
def info():
    return flask.render_template('info.html')

@app.route('/pledge/')
def pledge():
    return flask.render_template('pledge.html')

@app.route('/game/')
def game():
    return flask.render_template('game.html')
  
@app.route('/contact/')
def contact():
    return flask.render_template('contact.html')

@app.route('/calculator/')
def calculator():
    return flask.render_template('calculator.html')


# Start the app running and listening on a known port

web.run(app)
