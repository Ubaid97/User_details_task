# User is asked to input the information being requested. the input value is then stored in a variable of type string or integer depending on the user's input
first_name = input("Please enter your first name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")

DOB = input("Please enter your date of birth in the format dd/mm/yyyy: ")
age = input("Please enter your age: ")

house_number = input("Please enter your house number: ")
address = input("Please enter the first line of your address: ")
postcode = input("Please enter your postcode: ")

ni = input("Please enter your NI number: ")

course = input("Please enter the course you are applying to: ")
qualification = input("Please enter your most recent qualification: ")

# User info displayed using f-strings for easy concatenation
print(f"Full name: {first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}")
# first name, middle name, and last name are each capitalised and concatenated

print(f"Date of birth: {DOB}")
print(f"Age: {age}")
print(f"Address: {str(house_number)} {address.capitalize()}")
# house_number variable will have an integer as value, so it's been casted into a string

# postcode and NI number have all of their characters converted to upper case
print(f"Postcode: {postcode.upper()}")
print(f"NI number: {ni.upper()}")

print(f"Course: {course.capitalize()}")
print(f"Most recent qualification: {qualification.capitalize()}")

