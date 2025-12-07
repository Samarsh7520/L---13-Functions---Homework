def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b 

def mul(a,b ):
    return a * b

print("Calculator App \n")

print("Enter your choice: \n 1. Addition 2. Subtraction 3. Division 4. Multiplication: \n")
ch= int(input(""))
n1=int(input("Enter the First Numbers: \n"))
n2=int(input("Enter the Second Number: \n"))
if ch==1:
    print("The Sum is ", add(n1,n2))
elif ch==2:
    print("The Difference is ", sub(n1,n2))
elif ch==3:
    print("The Quotient is ", div(n1,n2))
elif ch==4:
    print("The Product is ", mul(n1,n2))