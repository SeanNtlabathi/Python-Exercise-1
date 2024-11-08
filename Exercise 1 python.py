# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name2=input ("enter your name :")

# TODO: Ask the user for their age and store it in a variable
age2=input ("enter your age :")

# TODO: Print a greeting using the name and age variables
print("hi my name is " + name2 + " and I am "  + age2) 

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length=int (input("enter the length of a rectang :"))

# TODO: Ask the user for the width of a rectangle and store it as an integer
width=int(input("enter the width of a rectangle :"))

# TODO: Calculate the area of the rectangle
area=int(length * width)

# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print("what is the temperature :")
celsius=float(input("celsius"))
user_temperature= celsius

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit= (celsius * 9/5) + 32

# TODO: Print the result rounded to two decimal places
#print("fahrenheit=" , + fahrenheit)
print(f"the fahrenheit is {round(fahrenheit, 2)}")
