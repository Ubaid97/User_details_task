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

print(f"Full name: {first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}")
print(f"Date of birth: {DOB}")
print(f"Age: {age}")
print(f"Address: {str(house_number)} {address.capitalize()}")
print(f"Postcode: {postcode.upper()}")
print(f"NI number: {ni.upper()}")
print(f"Course: {course.capitalize()}")
print(f"Most recent qualification: {qualification.capitalize()}")

