def carbon_car(miles, type, carbon):
  if type == 1 : 
    carbon += 0 
  elif type == 2 :
    carbon += 0.2 * miles 
  elif type == 3 : 
    carbon += 0.12 * miles
  elif type == 4 : 
    carbon += 0.105 * miles 
  elif type == 5 :
    carbon += 0.08 + miles


def carbon_bus(miles, how_often, carbon):
  carbon += 52 * miles * how_often * 0.5 * 0.1

def carbon_train(miles, how_often, carbon):
  carbon += 52 * miles * how_often * 10/6 * 0.0336