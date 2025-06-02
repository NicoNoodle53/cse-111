import math

#Get the information for the tire
width = int(input("Enter the width of the tire in mm: "))
aspect = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

#calculate the volume of the tire
volume = ((math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter))/ 10000000000)

#display results
print(f"The approximate volume is {volume:.2f} liters")

#get the date
from datetime import datetime
current_date = datetime.now()


#ask if theyi would like to buy a tire and get there phone number if they do
answer = input("Would you like to buy a tire with the dimensions entered (yes/no): ")
if answer == "yes":
    phone = (input("Enter your phone number(***-***-****): "))
    #append the informatino to a txt document
    with open("volumes.txt","at") as txt_file:
        print(f"{current_date:%Y-%m-%d} , {width} , {aspect} , {diameter} , {volume:.2f} , {phone}", file=txt_file)
#if they don't want to buy don't get there phone number
else:
    with open("volumes.txt","at") as txt_file:
        print(f"{current_date:%Y-%m-%d} , {width} , {aspect} , {diameter} , {volume:.2f} ", file=txt_file)



    

