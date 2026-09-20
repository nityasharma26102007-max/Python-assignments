#Calculator assignment 1


print("calculator")
print("the operation whatever u want")
num1 = int(input("enter the value num1"))
num2 = int(input("enter the value num2"))
operator = input("+,*,-,/")
if operator == '+':
    print("result",num1 + num2)
elif operator == '-':
    print("result",num1 - num2)
elif operator == '*':
    print("result",num1 * num2)
elif operator == '/':
    print("reslul",num1 / num2)
else:
    print("it is invalid operation")

#fever assignment 2

temp = int(input("enter the digits of temp - "))
print("enter ur body temperature", temp,"°C")
if(temp > 102 ):
    print("extremely hingh fevtemper")
elif(102 > temp > 97):
    print("mild fever")
elif(97 > temp > 37):
    print("normal temperature ")
else:
    print("consern to the doctor")

#C to F


celsius = float(input("enter the digit of celsius"))
print("entered Celsius is",celsius,"°C")
F = (celsius * 9/5) + 32 
print(F)
K=(celsius+273.15)
print(K)

# shree aradhya charya 




a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
D = (b**2)-(4*a*c)
root1 = -b + (D**2)/2*a
root2 = -b - (D**2)/2*a
print("root1 = ", root1)
print("root2 = ", root2)

    
