from replit import web
import flask
app = flask.Flask(__name__)

#displays home page
@app.route('/')
def index():
  return flask.render_template('index.html')

#displays information page
@app.route('/info/')
def info():
    return flask.render_template('info.html')

#displays pledge page
@app.route('/pledge/', methods =['GET','POST'])
def pledge():
  if flask.request.method == "POST":
    print(flask.request.form.getlist('pledges'))
    return 'Your pledges have been recorded'
  return flask.render_template('pledge.html')

#second route for pledge page writes data from
#pledge form to /data/pledgesmade.json File
#@app.route('/send_pledge/', methods = ['POST'])
#def send_pledge():    
  #pledges=flask.request.form['pledges']
  #pledgefile = open("data.pledgesmade.json", "a")
  #pledgefile.write(pledges)
  #message = "Your pledge has been recorded"
  #print(message)
  #return flask.render_template("index.html")
  
    
#displays contact page 
@app.route('/contact/')
def contact():
    return flask.render_template('contact.html')

#displays calculator page
@app.route('/calculator/' , methods = ['GET' , 'POST'])
def calculator():

  #if (request.method == "POST") and ('driven_miles' in request.form) and ('type_car' in request.form):
   # how_many_car = float(request.form.get('driven_miles'))
    #type_car = float(request.form.get('type_car'))
  
  
  return flask.render_template('calculator.html')

#displays leaderboard
@app.route('/leaderboard/')
def leaderboard():
    return flask.render_template('leaderboard.html')

#displays scores from quiz and pledge page
@app.route('/your_scores/',methods=["GET", "POST"])
def your_scores():
  return flask.render_template('your_scores.html')

#displays information about queen queens team
@app.route('/green_queens/')
def green_queens():
  return flask.render_template('green_queens.html')

#displays quiz page
@app.route('/quiz/')
def quiz():
  return flask.render_template('quiz.html')

# Start the app running and listening on a known port
#must be here or app wont Run

web.run(app)
