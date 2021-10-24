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
  pledgesresult=[]
  if flask.request.method == "POST":
    #print(flask.request.form.getlist('pledges'))
    pledgesresult = flask.request.form.getlist('pledges')
    print(pledgesresult)
    #open file object and write to pledgesmade
    #file.
    with open('data/pledgesmade.txt','w') as f:
      f.write(str(pledgesresult))
      print(pledgesresult)
    #now flash message to user to say that pledges
    #have been recorded.
    
    #return '<h4>Your pledges are <br> {} </h4>'.format(pledgesresult,sep=',')
    
  return flask.render_template('pledge.html', pledgesresult=pledgesresult)
  
    
#displays contact page 
@app.route('/contact/')
def contact():
    return flask.render_template('contact.html')

#displays calculator page
@app.route('/calculator/', methods = ['GET','POST'])
def calculator():
 # Values needed in the calculator
  fly_co2 = 0.115 
  fly_speed = 1000
  global carbon_emission , carbon_emission_travel , carbon_emission_diet, carbon_emission_diet
  
  

# Making sure the form was filled in with all the relevant values 
  if flask.request.method == "POST":
    how_long_car = float(flask.request.form.get('driven_miles'))
    type_car = int(flask.request.form.get('type_car'))
    bus_how_many = float(flask.request.form.get('bus_how_many'))
    bus_how_long = float(flask.request.form.get('bus_how_long'))
    train_how_many = float(flask.request.form.get('train_how_many'))
    train_how_long = float(flask.request.form.get('train_how_long'))
    fly_how_long = float(flask.request.form.get('fly_how_long'))
    diet_type = float(flask.request.form.get('diet_type'))
    energy_usage = float(flask.request.form.get('energy_usage'))
    energy_type = float(flask.request.form.get('energy_type'))

    carbon_emission = ''
    carbon_emission_travel = ''
    carbon_emission_diet = ''
    carbon_emission_energy = ''

    if type_car == 1: 
      carbon_emission_travel = (fly_how_long * fly_speed * fly_co2) + (train_how_long * 52 * train_how_many * 0.0366 * 10/6) + (bus_how_long * 52 * bus_how_many * 0.1 * 0.5)
      if (diet_type == 1) :
        carbon_emission_diet = 2049 
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return ''' <h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12* energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


      elif (diet_type == 2):
        carbon_emission_diet =  1387
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




      elif (diet_type == 3):
        carbon_emission_diet =  1052
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




    elif type_car == 2:
      carbon_emission_travel = (0.2 * how_long_car) + (fly_how_long * fly_speed * fly_co2) + (train_how_long * 52 * train_how_many * 0.0366 * 10/6) + (bus_how_long * 52 * bus_how_many * 0.1 * 0.5)
      if (diet_type == 1) :
        carbon_emission_diet = 2049 
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 *  energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

      elif (diet_type == 2):
        carbon_emission_diet =  1387
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




      elif (diet_type == 3):
        carbon_emission_diet =  1052
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)








    elif type_car == 3 : 
      carbon_emission_travel = (0.12 * how_long_car) + (fly_how_long * fly_speed * fly_co2) + (train_how_long * 52 * train_how_many * 0.0366 * 10/6) + (bus_how_long * 52 * bus_how_many * 0.1 * 0.5)
      if (diet_type == 1) :
        carbon_emission_diet = 2049 
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
      elif (diet_type == 2):
        carbon_emission_diet =  1387
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




      elif (diet_type == 3):
        carbon_emission_diet =  1052
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)






    elif type_car == 4 : 
      carbon_emission_travel = 0.105 * how_long_car + fly_how_long * fly_speed * fly_co2 + train_how_long * 52 * train_how_many * 0.0366 * 10/6 + bus_how_long * 52 * bus_how_many * 0.1 * 0.5
      if (diet_type == 1) :
        carbon_emission_diet = 2049 
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
      elif (diet_type == 2):
        carbon_emission_diet =  1387
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




      elif (diet_type == 3):
        carbon_emission_diet =  1052
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)





    elif type_car == 5 :
      carbon_emission_travel = (0.08 * how_long_car) + (fly_how_long * fly_speed * fly_co2) + (train_how_long * 52 * train_how_many * 0.0366 * 10/6) + (bus_how_long * 52 * bus_how_many * 0.1 * 0.5)
      if (diet_type == 1) :
        carbon_emission_diet = 2049 
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)
      elif (diet_type == 2):
        carbon_emission_diet =  1387
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




      elif (diet_type == 3):
        carbon_emission_diet =  1052
        if energy_type == 1:
          carbon_emission_energy = 0.997 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 2:
          carbon_emission_energy = 0.408 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


        elif energy_type == 3 :
          carbon_emission_energy = 0.861 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

        elif energy_type == 4 :
          carbon_emission_energy = 0.2 * 12 * energy_usage
          carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
          return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)






   






    elif (diet_type == 2):
      carbon_emission_diet =  1387
      if energy_type == 1:
        carbon_emission_energy = 0.997 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


      elif energy_type == 2:
        carbon_emission_energy = 0.408 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


      elif energy_type == 3 :
        carbon_emission_energy = 0.861 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

      elif energy_type == 4 :
        carbon_emission_energy = 0.2 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)




    elif (diet_type == 3):
      carbon_emission_diet =  1052
      if energy_type == 1:
        carbon_emission_energy = 0.997 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


      elif energy_type == 2:
        carbon_emission_energy = 0.408 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)


      elif energy_type == 3 :
        carbon_emission_energy = 0.861 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)

      elif energy_type == 4 :
        carbon_emission_energy = 0.2 * 12 * energy_usage
        carbon_emission = carbon_emission_diet + carbon_emission_energy + carbon_emission_travel 
        return '''<h4>Your carbon footprint is {} </h4>  <br> 
    <p>Let's break it down: </p>
    <ul>
    <li> Travel : {}  </li> 
    <li> Diet : {} </li> 
    <li> Energy : {} </li> 
    </ul>
    '''.format(carbon_emission , carbon_emission_travel, carbon_emission_diet, carbon_emission_energy)









  
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
  
@app.route('/your_scores_profile/')
def your_scores_profile():
  return flask.render_template('your_scores_profile.html')


# Start the app running and listening on a known port
#must be here or app wont Run

web.run(app)
