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
  
@app.route('/contact/')
def contact():
    return flask.render_template('contact.html')

@app.route('/calculator/')
def calculator():
    return flask.render_template('calculator.html')
#logic goes into here 
@app.route('/leaderboard/')
def leaderboard():
    return flask.render_template('leaderboard.html')

@app.route('/your_scores/')
def your_scores():
  return flask.render_template('your_scores.html')

@app.route('/green_queens/')
def green_queens():
  return flask.render_template('green_queens.html')

@app.route('/quiz/')
def quiz():
  return flask.render_template('quiz.html')

# Start the app running and listening on a known port

web.run(app)
