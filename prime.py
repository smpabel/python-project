
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: ")) 
count=0
   #Iterate from 2 to n / 2  
for num in range(lower,upper+1):  #10--20
    for i in range(2, num): 
            
        # If num is divisible by any number between  
        # 2 and n / 2, it is not prime  
        if (num % i) == 0: 
            print(num, "is not a prime number") 
            break
    else: 
        print(num, "is a prime number")
        count+=1
print("total prime number form",lower,"to",upper,"is: ",count)
 