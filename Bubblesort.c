
#include<stdio.h>
void main(){
int n,temp;
printf("Enter size of array : \n");
scanf("%d",&n);
int a[n],item;
for(int i=0;i<n;i++){
    printf("Enter Element %d : ",i+1);
    scanf("%d",&a[i]);
}
printf("Input array is : \n");
for(int i=0;i<n;i++){
printf("%d ",a[i]);
}

for (int i=0;i<n;i++){
    for(int j=0;j<n-i-1;j++){
        if (a[j]>a[j+1]){
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }
    }
}
printf("\nOutput array is : \n");
for(int i=0;i<n;i++){
printf("%d ",a[i]);
}
}
