def merge_sort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,arr)

def merge(arr1,arr2,ar):
    i=j=k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            ar[k]=arr1[i]
            i+=1
        elif arr1[i]>arr2[j]:
            ar[k]=arr2[j]
            j+=1
        k+=1
    while i<len(arr1):
        ar[k]=arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        ar[k]=arr2[j]
        j+=1
        k+=1
test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

for arr in test_cases:
    merge_sort(arr)
    print(arr)
#print(merge_sort([23, 18, 34, 17, 14, 20, 1, 9]))