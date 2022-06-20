#include <stdio.h>
int main(){
    int n ,i, largest, second,temp;
    int arr[10]={1,20,6,9,8,7,3,10,15};

    largest = arr[0];
    second = arr[1];

    if(largest<second){
        temp=largest;
        largest=second;
        second=temp;
    }

    for ( i = 2; i < 10; i++)
    {
        if(arr[i] >= largest) {
        second = largest;
        largest  = arr[i];
        }    
        else if(arr[i]>=second) {
        second  = arr[i];
        }

    }
    
    printf("Largest element = %d",largest );
    printf("\nsecond largest value is= %d",second);

    return 0;
}