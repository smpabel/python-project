#include<stdio.h>
int main(){

    int i,n,sum=0;
    printf("Enter integer number: ");
    scanf("%d",& n);

    for ( i = 1; i<=n; i++)
    {
        sum = sum + i;
    }
    printf("Summation of 1+2+3+....+%d is = %d" ,n,sum);

    //1+ 1/2 + 1/3 + ..... 1/n =?
    
    float s=0.0, j, carry;
    for ( j = 1; j <=n; j++)
    {
        carry = 1/j;  //1/1=1, 1/2=0.5,   1/3=0.33
        s = s+carry;  //0+1=1, 1+0.5=1.5  1.5+0.33=1.83
    }

    printf("\n1+ 1/2 + 1/3 + ..... 1/%d  is = %.2f",n,s);
    
    return 0;
}