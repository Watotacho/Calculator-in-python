# creating  calculator using python
#keyword def is used to define a function
def add(a,b):
    result=a+b
    print(result)
    #code for addition

def sub(a,b):
    result=a-b
    print(result)
    #code for subtraction
def mul(a,b):
    result=a*b
    print(result)
    #code for multiplication
def div(a,b):
    result=a/b
    print(result)
    #code for division
a=int(input("Enter the first number: "))
b=int(input("Enter the second number "))
op=input("Enter the operator: ")#enter operators such as -,+,/,*
#if and elif allow us to check for multiple expression
#checks if the condition is true or false
if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid Operator")


