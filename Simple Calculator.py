
print("Welcome to the Simple Calculator")

number1=float(input("Enter first number: "))
operator=input("enter an operator : +, -, *, /, % ")
number2=float(input("Enter the second number: "))

if operator =="+":
    print("result is : ", number1+number2 )
elif operator == "-":
    print("result is : ", number1-number2 )
elif operator == "*":
    print("result is : ", number1*number2)
elif operator =="%":
    print ("result is : ", number1%number2)
elif operator =="/":
    if number2 !=0:
        print("result is : ", number1/number2)
    else:
        print("you can not divide by Zero")
else:
    print("invalid operator")

