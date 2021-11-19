import array

# for loop

a = array.array('i',[])
n = int(input("Enter number of element u want to input: "))

for i in range(n):
    a.append(int(input("Enter value: ")))

for i in range(len(a)):
    
    print(i, "index = ", a[i])

# while loop
ar = array.array('i',[])
n = int(input("Enter number of elements u want to input: "))

i = 0
j = 0

while i<n:
    ar.append(int(input("Enter value: ")))
    i+=1

while j<len(ar):
    print(j, "index = ", ar[j])
    j+=1



