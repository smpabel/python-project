from numpy import*
a = array([10,200,300,400,50]) 
b = array([100,200,30,400,500]) 

result = where(a>b,a,b) # if true than a else b
print(result)

c = a.view() # a er mirror view
print(a)
print(c)
print(id(c))
print("a id",id(a))



