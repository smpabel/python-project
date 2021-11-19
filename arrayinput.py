from numpy import *
n = int(input("Enter number of elements: "))
a = zeros(n,dtype=int)
print(a)

for i in range(n):
    x = int(input("Enter value: "))
    a[i] = x

print(a)

for i in range(len(a)):
    print(i, "Index = ", a[i])

a = int(input("enter number: "))
for i in range(a):
    s = int(input("enter value: "))
    i = s
    print(i)






