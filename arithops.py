result = 0
no1 = int(input("Enter first number"))
no2 = int(input("Enter second number"))
op = input("Enter operator")

if op=='+':
    result=no1+no2
if op=='-':
    result= no1-no2
if op=='*':
    result=no1*no2
if op=='/':
    result=no1/no2

print("result= ",result)


