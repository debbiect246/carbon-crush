#Carbon footprint calculator of an individual or family.
print("Welcome to the Carbon Crushers Carbon Calculator. Please provide the following details");
carbon_emission=0.0
family_members=float(input("Enter family members"))
food=float(input("if you are a non-vegetarian then input 1"))
calories=float(input("Enter average calories"))
if(food==1):
    carbon_emission += (calories*0.01)*family_members
else:
    carbon_emission += (calories*0.005)*family_members
driven_miles=float(input("Enter avg kms driven in a year"))
if(driven_miles>0):
    carbon_emission += driven_miles*0.01
else:
    print("enter valid kms driven")
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