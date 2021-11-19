from numpy import*
ar = array([10,20,30,50,60,70])
n = (len(ar))
print(n)
for i in range(n):
    print(i,"index = ",ar[i])
print("****************************************************")

l = linspace(1,10,11) # 1 teke 10 ke total 11 vage vag korse
s = len(l)
for i in range(s):
    print(i," linspace index = ",l[i])

print("****************************************************")

log = logspace(1,3,5) #log jar base default 10.0 thake start 10^1 end 10^3, 5 vage vag korbe
s = len(log)
for i in range(s):
    print(i,"log index = ",log[i])

# arange function
a = arange(1,10)
print("arange",a)

a = zeros(10, dtype=int)
print(a)

a = ones(10,dtype=int)
print(a)



