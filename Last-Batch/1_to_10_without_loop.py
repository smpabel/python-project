
#without loop
def number(initial,last):
    
    if(initial<=last):
        print(initial)
        number(initial+1,last)#recursive function  
number(1,10)


#with loop
for i in range(1,11):
    print(i)
    i+=1

    