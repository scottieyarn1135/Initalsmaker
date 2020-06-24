
#Using sleep to add a delay in between prints I don't need them but I thought they added to the application and so I can test out delays.
from time import sleep
#When the application name appears in the print it will say the name of the application.
application_name = "inital maker 3000"
#when the AI name is appears in the print it will say the name of the AI.
ai_name = "Billy"

# Start of the app This is mostly to simulate an AI walking you though a process to get the initals of your name.
print("Hello and Thank you for using "+ application_name.upper() + " I am your trusty RO----AI friend..." )
sleep(2)
print(ai_name.upper())
sleep(2)
print("Okay let's get started I will be need both your first name and last name...")
sleep(2)

#This let's the user input a first name and last name.
first_name = input(str("Enter First Name Here: "))
last_name = input(str("Enter Last Name Here: "))

#This grabs the first character of the string for example if the first one is A it will grab A if it is B it will grab B so on and so on.
first_letter = first_name[0]
last_letter = last_name[0]
# it will say Hello to the person using both there first name and last name.
print("Hello " + first_name +" "+ last_name)
sleep(1.5)
print("Let me make your initials!")
sleep(3)
print("Here are your initials!")
sleep(1.5)
#This prints the first letter of the first name and of the last name.
print(first_letter + last_letter)
sleep(3)
print("Now creating file!")
sleep(2)
#This will create a file called inital.txt this will have text written to the file thanking the user for using the app and it will give them there initals.
with open("inital.txt", mode="w") as f:
    f.write("Thank you for using "+ application_name + " This file contains your inital don't lose it! \n" + first_letter + last_letter +"\nWe hope you enjoyed using this product!")
#This is a thank you message for the user for using the application.
print("Thank you for using " + application_name.upper() + " Hope you enjoyed using it!")
sleep(5)
