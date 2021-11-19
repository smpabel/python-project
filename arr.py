import array

a = array.array('i',[10,20,30,40,50,])
b = array.array('i',[60,70,80])
for i in (a):
    print(i)

a.insert(1, 222)
for i in (a):
    print("skafhgklsafhg",i)

a.remove(40)
for i in (a):
    print(i)


print(a.index(20))

a.reverse()
for i in (a):
    print("Reverse",i)

a.extend(b)
for i in (a):
    print("Extends",i)

c = array.array('i',[60,70,80,90,100,110,120])
for i in c:
    print(i)
sc = c[1:5]
for i in sc:
    print("Sclice part",i)
