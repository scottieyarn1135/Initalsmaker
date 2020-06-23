from time import sleep

application_name = "inital maker 3000"
ai_name = "Billy"
print("Hello and Thank you for using "+ application_name.upper() + " I am your trusty RO----AI friend..." )
sleep(2)
print(ai_name.upper())
sleep(2)
print("Okay let's get started I will be need both your first name and last name...")
sleep(2)
first_name = input(str("Enter First Name Here: "))
last_name = input(str("Enter Last Name Here: "))

first_letter = first_name[0]
last_letter = last_name[0]

print("Hello " + first_name +" "+ last_name)
sleep(1.5)
print("Let me make your initials!")
sleep(3)
print("Here are your initials!")
sleep(1.5)
print(first_letter + last_letter)
sleep(0.5)
print("Thank you for using " + application_name.upper() + " Hope you enjoyed using it!")
