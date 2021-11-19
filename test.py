ab = [10,20,20,30]
print (type(ab))
b = ab #Aliasing
print(id(b))
print(id(ab))

# Tuple  not modifiable 
a = (10,20,30,(50,60))
n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i,j,"=",a[i][j])

    else:
        print(i,a[i])

ab.append((50,60))
ab.append(90)
print(ab)
print(type(ab))
print(type(a))
print(type(a[0]))

print()

c = ([10,20],[30,40]) #tuple of list
print(type(c))
c[0][1]=90 #tuple modify hocche na only tuple er moddhe list modify hocche
print(c)

# Dictionary
s = {101:"A",102:"B",103:"C",104:"sm pabel"}
print(s)
n = (input("Enter a Id for search: "))
for key,value in s.items():
    if n==value:
        print(n,"your value is: ",key)

