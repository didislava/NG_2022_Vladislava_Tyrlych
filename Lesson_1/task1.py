import math
print("for using √ enter // as operation and 1 as second number")
print("for using ^ enter 2 as second number")
first_number = int(input("enter 1st number "))
operation = input("operation (+,-,*,/) ")
second_number = int(input("enter 2nd number "))


if operation == "+":
    print("result = " + str(first_number+second_number))

if operation == "-":
    print("result = " + str(first_number-second_number))

if operation == "*":
    print("result = " + str(first_number*second_number))

if operation == "/":
    print("result = " + str(first_number/second_number))

if operation == "//":
    print("result = " + str(math.sqrt(first_number)))

if operation == "^":
    print("result = " + str(first_number*first_number))
