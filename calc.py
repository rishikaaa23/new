def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b



print("basic calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")


choice=int(input("enter the choice"))

a=int(input("enter the first number"))
b=int(input("enter the second number"))



if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))

else:
    print("enter a valid choice!")