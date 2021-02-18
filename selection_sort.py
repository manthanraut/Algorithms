l=[23, 18, 34, 17, 14, 20, 1, 9]
for i in range(len(l)):
    min_index=i
    for j in range(i,len(l)):
        if l[j]<l[min_index]:
            min_index=j
    if i!=min_index:
        l[i],l[min_index]=l[min_index],l[i]
print(*l)

