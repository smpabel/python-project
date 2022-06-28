//using recursion function
#include<stdio.h>
long double fact(), x;
int main(){

    int n;
    printf(" Enter the Number to Find Factorial :");
    scanf("%d",&n);
 
    x=fact(n);
    printf(" Factorial of %d is %Lf", n,x);
 
    return 0;
}

long double fact(int n){
    if(n==0)
        return(1);
    return(n*fact(n-1));
}



    
