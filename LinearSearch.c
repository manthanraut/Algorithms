#include<stdio.h>
void main(){
int n,item;
printf("Enter size of array : \n");
scanf("%d",&n);
int arr[n];
for(int i=0;i<n;i++){
    printf("Enter Item %d :\n",i+1);
    scanf("%d",&arr[i]);
}
printf("Enter value to be searched  :\n");
scanf("%d",&item);
for(int i=0;i<n;i++){
    if (arr[i]==item){
        printf("Item found at position %d\n",i+1);
    }
}

}
