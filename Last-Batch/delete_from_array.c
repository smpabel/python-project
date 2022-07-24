#include<stdio.h>
int main(){
   int student[40],pos,i,size;

   printf("enter no of elements in array of students:");
   scanf("%d",&size);

   printf("enter %d elements are:\n",size);
   for(i=0;i<size;i++)
      scanf("%d",&student[i]);

   printf("enter the position where you want to delete the element:");
   scanf("%d",&pos);

   for(i=pos-1;i<=size-1;i++)
      student[i]=student[i+1];
   
   printf("final array after inserting the value is\n");
   for(i=0;i<size-1;i++)
      printf("%d\n",student[i]);
   return 0;
}