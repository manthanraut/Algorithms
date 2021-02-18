def binary_search(elements,item,start,end):
    while(start<=end):
        mid=(start+end)//2
        if elements[mid]==item:
            return True
        if item<elements[mid]:
            end=mid-1
        elif item>elements[mid]:
            start=mid+1
    return False
l=[1, 4, 9, 17, 18, 20, 23, 34]
if binary_search(l,34,0,len(l)-1):
    print("Element exist")
else:
    print("Not Found")