#Imported Modules
from time import sleep

# Variables
application_name = "inital maker 3000"
ai_name = "Billy"

# Start of the app
print("Hello and Thank you for using "+ application_name.upper() + " I am your trusty RO----AI friend..." )
sleep(2)
print(ai_name.upper())
sleep(2)
print("Okay let's get started I will be need both your first name and last name...")
sleep(2)

#This let's the user input a first name and last name.
first_name = input(str("Enter First Name Here: "))
last_name = input(str("Enter Last Name Here: "))

#This grabs the first character of the string.
first_letter = first_name[0]
last_letter = last_name[0]
print("Hello " + first_name +" "+ last_name)
sleep(1.5)
print("Let me make your initials!")
sleep(3)
print("Here are your initials!")
sleep(1.5)
print(first_letter + last_letter)
sleep(3)
print("Now creating file!")
sleep(2)
#This will create a file called inital.txt this will have text written to the file.
with open("inital.txt", mode="w") as f:
    f.write(f'''Thank you for using {application_name} {first_name} {last_name} 
                This file contains your inital don't lose it!\n{first_letter}{last_letter}
                We hope you enjoyed using this product!''')
print("Thank you for using " + application_name.upper() + " Hope you enjoyed using it!")
sleep(5)
