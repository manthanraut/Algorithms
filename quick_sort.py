def quick_sort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quick_sort(arr,start,pi-1)
        quick_sort(arr,pi+1,end)
def partition(arr,start,end):
    pivot_index=start
    pivot=arr[pivot_index]
    while(start<end):
        while start<len(arr) and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[pivot_index],arr[end]=arr[end],arr[pivot_index]
    return end
test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

for arr in test_cases:
    quick_sort(arr,0,len(arr)-1)
    print(arr)