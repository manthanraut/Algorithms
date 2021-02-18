l=[23, 18, 34, 17, 14, 20, 1, 9]
for i in range(1,len(l)):
    anchor=l[i]
    j=i-1
    while j>=0 and anchor<=l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=anchor
print(*l)