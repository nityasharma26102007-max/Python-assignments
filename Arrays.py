#midle of arr
arr = [2,3,6,4,5]
n = 3
start=0
end=len(arr)-1
s = sorted(arr)
print(s)
i=0
while(start<=end):
    mid = start+end//2
    if arr[mid]==n:
        print("found",mid)
        break
    elif arr[mid]<n:
        start=mid+1
    else:
        end=mid-1


#exract
n = [1,2,3,4,5]
print(n[2])

#exract
import numpy as np
arr3d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
    ])
    
print(arr3d)

#
import array
arr=array.array('i',[1,2,3])
print(arr)

#
import numpy as np
arr=np.array([1,2,3,4])
m = arr*2
print(m)

#
arr = [1,2,3]
print(arr)
arr=[1,2,3,4,5]
for i in range(len(arr)):
    print(arr[i])

#
arr = [1,2,3,4,5]
for i in range(len(arr)):
    print(arr[i],end=' ')
def add(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    print(sum)
    return 
add(arr = [1,2,3,4])
print(add)

#
def reverse(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end=" ")
    return
    
reverse(arr = [1,2,3,4])
print(reverse)
def c(arr):
    count=0
    for i in arr:
        if i%2!=0 :
            count=count+1
    print(count)
    return
c(arr = [6,3,4,7])
print(c)

#
def frequency(n):
    count=0
    for i in arr:
        if n==i :
            count=count+1
    print(count)
    return
arr=[1,2,3,3,4,5,3,6,7]
frequency(3)
print(frequency)


#
n=int(input("enter the num"))
for i in range(1,n+1):
    print(i,end=" ")
    
n = []
print("any 10 num")
for i in range(10):
    num=int(input(f"enter num {i+1}:"))
    n.append(num)
print(n)
n = []
print("any 10 num")
for i in range(10):
    num=int(input(f"enter num {i+1}:"))
    n.append(num)
print(n)
s = sum(n)
print(s)
a = [1,3,2,4]
a1 = []
for i in a:
    s=a.append(a1)
print(s)
a = [4,2,5,3,6,9]
s=5
for i in range(len(a)):
    if a[i]==s:
        print(i)
