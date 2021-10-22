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
  global pledgesresult
  if flask.request.method == "POST":
    #print(flask.request.form.getlist('pledges'))
    pledgesresult = flask.request.form.getlist('pledges')
    #open file object and write to pledgesmade
    #file.
    with open('data/pledgesmade.txt','w') as f:
      f.write(str(pledgesresult))
    #now flash message to user to say that pledges
    #have been recorded and render scores page.
    return '<h4>Your pledges are {} </h4>'.format(pledgesresult)
  return flask.render_template("pledge.html")

@app.route('/show_pledges/', methods = ['GET', 'POST'])
def show_pledges():
  if flask.request.method == "POST":
    pledgesresult = flask.request.form.getlist('pledges')
    with open('data/pledgesmade.txt', 'r') as f:
      f.read(str(pledgesresult))
    return '<h4>Your pledges are {} </h4>'.format(pledgesresult)
    return flask.render_template('your_scores.html')
  
    
  

    
#displays contact page 
@app.route('/contact/')
def contact():
    return flask.render_template('contact.html')

#displays calculator page
@app.route('/calculator/', methods = ['GET','POST'])
def calculator():
 # Values needed in the calculator
  carbon_emission = 0
  fly_co2 = 0.115 
  fly_speed = 1000


# Making sure the form was filled in with all the relevant values 
  if flask.request.method == "POST":
    how_long_car = int(flask.request.form.get['driven_miles'])
    type_car = flask.request.form.get['type_car']
    bus_how_many = flask.request.form.get['bus_how_many']
    bus_how_long = flask.request.form.get['bus_how_long']
    train_how_many = flask.request.form.get['train_how_many']
    train_how_long = flask.request.form.get['train_how_long']
    fly_how_long = flask.request.form.get['fly_how_long']



    if type_car == 1 : 
      carbon_emission = fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5
      return '<h4>Your carbon emissions are {} </h4>'.format(carbon_emission)
    elif type_car == 2 :
      carbon_emission = 0.2 * how_long_car + fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5
    elif type == 3 : 
      carbon_emission = 0.12 * how_long_car + fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5
    elif type == 4 : 
      carbon_emission = 0.105 * how_long_car + fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5
    elif type == 5 :
      carbon_emission = 0.08 + how_long_car + fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5

    #carbon_emission += bus_how_long * 52 * bus_how_many * 0.1 * 0.5
    #carbon_emission += train_how_long * 52 * train_how_many * 0.0366 * 10/6
    #carbon_emission += fly_how_long * fly_speed * fly_co2








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

@app.route('/game_home/')
def qhome():
  return flask.render_template('quiz_home.html')
  



# Start the app running and listening on a known port
#must be here or app wont Run

web.run(app)
