#include<stdio.h>
int main(){
    
    int i,n,sum=0, missing;
    printf("\nEnter the size of array ");
    scanf("%d",&n);
    int arr[n-1];
    printf("Enter value to add in the array \n");
    for ( i = 0; i < n-1; i++)
    {
        /* code */
        scanf("%d",&arr[i]);
        sum= sum+arr[i];
    }
    printf("summation of entered array is = %d",sum);
    //find missing number tricks
    missing = (n*(n+1))/2;
    printf("\nsummation of actual n number is %d and  missing number is = %d",missing, missing-sum);

    

    //given array summation and avarage tricks

    float s= 0;
    float values[10]={1,2,3,4,5,6,7,8,9,10};
  
    for(int i = 0; i <10; ++i) {

        s = s+values[i];
    }
    printf("\n\n\nsummation of given array is : %.2f", s);
    float avg = s/10;
    printf("\nAverage of given array is : %.2f", avg);




return 0;
    


}