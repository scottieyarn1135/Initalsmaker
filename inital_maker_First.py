# Imported Modules
import time
# Variables of app names
application_name = "inital maker 3000"
ai_name = "Billy"
# Start of the app
def Introduction():
    print(f"Hello and Thank you for using {application_name.upper()} I am your trusty RO----AI friend...")
    time.sleep(2)
    print(ai_name.upper())
    time.sleep(2)
    print("Okay let's get started I will be need both your first name and last name...")
    time.sleep(2)

Introduction()
# Variables for name and initals.
first_name = input(str("Enter First Name Here: "))
last_name = input(str("Enter Last Name Here: "))
first_letter = first_name[0]
last_letter = last_name[0]

def inital():
    print(f"Hello {first_name} {last_name}")
    time.sleep(1.5)
    print("Let me make your initials!")
    time.sleep(3)
    print("Here are your initials!")
    time.sleep(1.5)
    print(f"{first_letter}{last_letter}")
    time.sleep(3)
    print("Now creating file!")
    time.sleep(2)

inital()
# This will create a file called inital.txt that prints the inital results.
def filemaker():
    with open('inital.txt', mode='w') as f:
        f.write(f"Thank you for using {application_name} {first_name} {last_name}!" 
                f"This file contains your inital don't lose it!\n{first_letter}{last_letter}\n"
                "We hope you enjoyed using this product!")
filemaker()
print(f"Thank you for using {application_name.upper()} Hope you enjoyed using it!")
time.sleep(5)