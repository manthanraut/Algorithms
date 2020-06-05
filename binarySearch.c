#include<stdio.h>
int sort(int a[],int);
int binarysearch(int a[],int n);
void main(){
int n;
printf("Enter size of array : \n");
scanf("%d",&n);
int a[n],index;
for(int i=0;i<n;i++){
    printf("Enter Element %d : ",i+1);
    scanf("%d",&a[i]);
}
printf("Input array is : \n");
for(int i=0;i<n;i++){
printf("%d ",a[i]);
}
int result[n];
result[n]=sort(a,n);
printf("\nOutput array is : \n");
for(int i=0;i<n;i++){
printf("%d ",a[i]);
}
index=binarysearch(a,n);
if(index!=-1)
printf("\nElement found at index %d",index);
else
    printf("\nElement not found in array");
}
int sort(int a[],int n){
    int temp;
for (int i=0;i<n;i++){
    for(int j=0;j<n-i-1;j++){
        if (a[j]>a[j+1]){
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }
    }
}
return a;
}

int binarysearch(int a[],int n){
    int item,up=n-1,low=0,mid;
printf("\nEnter element to be searched : \n");
scanf("%d",&item);
while(up>=low){
mid=((up-1)+low)/2;
if (a[mid]==item)
    return(mid);
    if(item>a[mid]){
        low=mid+1;
    }
    else{
        up=mid-1;
    }
}
return -1;
}
