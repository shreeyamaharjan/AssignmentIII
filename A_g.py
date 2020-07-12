def interpolationSearch(lst,key):
    l=0
    h=n-1
    while l<=h and key>=lst[l] and key <=lst[h]:
        index=l+int((float(key-lst[l])/(lst[h]-lst[l]))*(h-l))
        if lst[index]==key:
            globals()['pos'] = index
            return True

        if lst[index]<key:
            l=index+1
        else:
            h=index-1
    return False

lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
lst.sort()
print("The  list is : \n", lst)
key = int(input("Enter the number you wanted to search for : "))
if interpolationSearch(lst,key):
    print("The key {} is found at {}".format(key,pos))

else:
    print("Element not found")