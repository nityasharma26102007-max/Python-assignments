#sq root
i=1
for i in range(1,11):
    print(i,'**2','=',i**2)
    i+=1

#cube root
i=1
for i in range(1,11):
    print(i,'**3','=',i**3)
    i+=1

#odd no.
for i in range(10,100):
    if(i %2 != 0):
        print(i)

#reverse no.
num =int(input("enter the num value"))
rev=0
while num>0 :
    rem=num%10
    rev=rev*10+rem
    num = num//10
print(rev)

