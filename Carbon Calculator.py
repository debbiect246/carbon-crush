




#Carbon footprint calculator of an individual or family.
print("Welcome to the Carbon Crush Carbon Calculator. Please provide the following details");
carbon_emission=0.0
family_members=float(input("Enter family members"))
food=float(input("if you are a non-vegetarian then input 1"))
calories=float(input("Enter average calories"))
if(food==1):
    carbon_emission += (calories*0.01)*family_members
else:
    carbon_emission += (calories*0.005)*family_members





# Use of Car 
drive_car = input("Do you drive a car? If yes, press 1. \n If not input any value (except a space): " )
if drive_car == '1' : 
# Checking the number of miles the person does if they have a car
  driven_miles=input("On average, how many kilometres do you drive a year? : ")
# This loop checks if a string contains a number (greate or equal to 0).
  if driven_miles.isdigit() == False :
    driven_miles=input("You've inputted an invalid result.Please enter how many kilometres do you drive a year on average (it needs to be a number)? : ")
    if(float(driven_miles) > 0):
      type_car = input("What type of car do you drive? \n 1 - Petrol \n 2 - Diesel \n 3 - Electric  \n 4 - Hybrid \n Enter the number which best fits your car. : ")
      if type_car == '1' : 
        carbon_emission += 0.2 * float(driven_miles) 
      elif type_car == '2' : 
        carbon_emission += 0.12 * float(driven_miles) 
      elif type_car == '3' : 
        carbon_emission += 0.105 * float(driven_miles)
      elif type_car == '4' : 
        carbon_emission += 0.1 * float(driven_miles)
      elif (type_car not in ['1','2','3','4']):
# Re-running the loop if they press a number other than 1,2 or 3
        type_car = input("That's not a type of car!! Please enter a number between 1 and 4 which best describes your car : ")
        if type_car == '1' : 
          carbon_emission += 0.2 * float(driven_miles)
        elif type_car == '2' : 
          carbon_emission += 0.12 * float(driven_miles)
        elif type_car == '3' : 
          carbon_emission += 0.105 * float(driven_miles)
        elif type_car == '4' : 
          carbon_emission += 0.1 * float(driven_miles)
    else : 
# Re-running the loop for kms driven if they press an invalid key. Making the instructions clearer so they don't make the mistake again
      driven_miles=input("You must drive your car somewhere!! Please enter a number greater than 0 of how many kilometres you drive a year on average : ")
      if ( float(driven_miles) > 0 ):
        type_car = input("What type of car do you drive? \n 1 - Petrol \n 2 - Diesel \n 3 - Electric \n 4 - Hybrid  \n Enter the number which best fits your car. : ")
        if type_car == '1' : 
          carbon_emission += 0.2 * float(driven_miles)
        elif type_car == '2' : 
          carbon_emission += 0.12 * float(driven_miles) 
        elif type_car == '3' : 
          carbon_emission += 0.105 * float(driven_miles)
        elif type_car == '4' : 
          carbon_emission += 0.1 * float(driven_miles)
        elif (type_car not in ['1','2','3','4']) : 
          type_car = input("That's not a type of car!! Please enter a number between 1 and 4 which best describes your car : ")
          if type_car == '1' : 
            carbon_emission += 0.2 * float(driven_miles)
          elif type_car == '2' : 
            carbon_emission += 0.12 * float(driven_miles)
          elif type_car == '3' : 
            carbon_emission += 0.105 * float(driven_miles)
          elif type_car == '4' : 
            carbon_emission += 0.1 * float(driven_miles)


  elif (float(driven_miles) > 0):
    type_car = input("What type of car do you drive? \n 1 - Petrol \n 2 - Diesel \n 3 - Electric \n 4 - Hybrid \n Enter the number which best fits your car. : ")
    if type_car == '1' : 
      carbon_emission += 0.2 * float(driven_miles) 
    elif type_car == '2' : 
      carbon_emission += 0.12 * float(driven_miles) 
    elif type_car == '3' : 
      carbon_emission += 0.105 * float(driven_miles)
    elif type_car == '4' : 
      carbon_emission += 0.1 * float(driven_miles)
    elif (type_car not in ['1','2','3', '4']):
# Re-running the loop if they press an invalid key. Making the instructions clearer so they don't make the mistake again
      type_car = input("That's not a type of car!! Please enter a number between 1 and 4 which best describes your car : ")
      if type_car == '1' : 
        carbon_emission += 0.2 * float(driven_miles)
      elif type_car == '2' : 
        carbon_emission += 0.12 * float(driven_miles)
      elif type_car == '3' : 
        carbon_emission += 0.105 * float(driven_miles)
      elif type_car == '4' : 
        carbon_emission += 0.1 * float(driven_miles)
  else : 
# Re-running the loop for kms driven if they press an invalid key. Making the instructions clearer so they don't make the mistake again
    driven_miles=input("You must drive your car somewhere!! Please enter a number greater than 0 of how many kilometres you drive a year on average : ")
    if ( float(driven_miles) > 0 ):
      type_car = input("What type of car do you drive? \n 1 - Petrol \n 2 - Diesel \n 3 - Electric  \n 4 - Hybrid \n Enter the number which best fits your car. : ")
      if type_car == '1' : 
        carbon_emission += 0.2 * float(driven_miles)
      elif type_car == '2' : 
        carbon_emission += 0.12 * float(driven_miles) 
      elif type_car == '3' : 
        carbon_emission += 0.105 * float(driven_miles)
      elif type_car == '4' : 
          carbon_emission += 0.1 * float(driven_miles)
      elif (type_car not in ['1','2','3', '4']): 
        type_car = input("That's not a type of car!! Please enter a number between 1 and 4 which best describes your car : ")
        if type_car == '1' : 
          carbon_emission += 0.2 * float(driven_miles)
        elif type_car == '2' : 
          carbon_emission += 0.12 * float(driven_miles)
        elif type_car == '3' : 
          carbon_emission += 0.105 * float(driven_miles) 
        elif type_car == '4' : 
          carbon_emission += 0.1 * float(driven_miles)






# Public transport 
# CO2 g/Km for trains and CO2 g/Mile for buses
bus_emission_by_mile = 0.1
train_emission_by_km = 0.0366

# Checks to see if the user uses public transport
public_transport = input("Do you use public transport? Press 1 if you do, otherwise press any key : ")
if public_transport == '1':

# Checks to see if the user takes the bus
  bus = input("Do you take the bus? Press 1 if you do, otherwise press any key : ")
  if bus == '1':
    
# Inputs how often they get the bus a week. Gives them another try if they inout an invalid response
    bus_how_often = input("On average, how many times do you take the bus a week? : ")
    if (bus_how_often.isdigit() == False) or (bus_how_often == '0'):
      bus_how_often = input("You've inputted an invalid value. Please enter how often you take the bus in a week (Must be a number greater than 0) : ")

# Inputs how long their average bus jounery is. Gives them another try if they inout an invalid response
    bus_how_long = input("What is the average length of your bus journey in minutes? : ")
    if (bus_how_long.isdigit() == False) or (bus_how_long == '0'):
      bus_how_long = input("You've inputted an invalid value. Please enter the average length of your bus journey in minutes (Must be a number greater than 0) : ")

# Assuming the average speed of a bus is 30mph
    carbon_emission += float(bus_how_long) * 52 * float(bus_how_often) + bus_emission_by_mile * 0.5

# Checks to see if they use the train / tube
  train = input("Do you take the tube / train ? Press 1 if you do, otherwise press any key except space : ")
  if train == '1':

# Inputs how often they get the train/tube a week. Gives them another try if they inout an invalid response
    train_how_often = input("On average, how many times do you take the train/tube a week? : ")
    if (train_how_often.isdigit() == False) or (train_how_often == '0'): 
      train_how_often = input("You've inputted an invalid value. Please enter how often you take the train/tube in a week (Must be a number greater than 0) : ")

# Inputs how long their average train/tube jounery is. Gives them another try if they inout an invalid response
    train_how_long = input("What is the average length of your train/tube journey in minutes? : ")
    if (train_how_long.isdigit() == False) or (train_how_long == '0'):
      bus_how_long = input("You've inputted an invalid value. Please enter the average length of your bus journey in minutes (Must be a number greater than 0) : ")

# Assuming a train travels at 100 km/hr
    carbon_emission += float(train_how_long) * 52 * float(train_how_often) + train_emission_by_km * (10/6)





# Flying 
#Checking to see if the user takes planes
fly = input("Do you often take a flight in a year? Press 1 if you do, if not press any key : ")
if fly == '1':
# Taking a rough average of how many hours they fly a year. Giving them one chance to enter an invalid response
  fly_hours = input("Roughly how many hours do you fly a year? You can add decimals into your answer. For example, you can write 0.5 for 30 minutes of flying : ")
  if (fly_hours.replace('.', '', 1).isdigit() == False ) or (fly_hours == '0') : 
    fly_hours = input("You've inputted an invalid value. Please enter the number of hours you fly roughly a year? (Needs to be a number greater than 0) : ")

# Assumption that a plane flies at 1,000 kmph and using that a passenger on average emits 115g of CO2 per KM on a flight 
carbon_emission += float(fly_hours) * 0.115 * 1000








household_utilities=float(input("Enter number of household utilities \nThey include 1)Electricity \n2)Natural Gas \n3)Fuel \n4)oil"))
total_expenditures=float(input("Enter total expenditures spent after the utilities"))
if family_members>0 and household_utilities>0 and total_expenditures>0:
    carbon_emission += (0.12*total_expenditures)*household_utilities
else:
    print("enter valid details")








Electricity = float(input("Enter the average monthly kilowatts per hour from your electric bill. "))*12
if Electricity < 0:
 print("Please enter a positive number. ")
elif Electricity==0:
 print("Are you sure you didn't use any electricity at all? Please enter a non-zero number. ")
else:
 print("For electricity, the amount of carbon dioxide released is: ", Electricity, "kg/yr")
carbon_emission += ((0.12*total_expenditures)*household_utilities)*family_members*Electricity
print("your carbon emissions are {} metric tonnes".format(carbon_emission))