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


#!

n = 10
for i in range(1,n):
    rem = i*(i+1)//2
    print(rem)
i=i+1

#write a program to print cube series from 45 to 57.
n1=45
n=57
for i in range(45,n+1):
    rem = i**3
    print(rem)
i=i+1

#scrapping

exp =[
    {
    "experiment ":"exp1",
    "reading ":(10,20,20,30),
    "status ":{"valid"}
    },
    {
        "experiment ":"exp2",
        "reading ":(5,5,10),
        "status ":{"outerlier","retry"}
        },
        {
            "experiment ":"exp3",
            "reading ":(40,50,50,60),
            "status":{"valid","retry"}
            }
    ]
for e in exp:
    e["reading "]=tuple(dict.fromkeys(e["reading "]))
print("Updated readings .")
for e in exp:
    print(e["reading "])
    



