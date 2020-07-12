def linearSearch(lst,key):
    for i in range (n):
        if key ==  lst[i]:
            print("The key element {} is found at index {} ".format(key,i))
            break
    else:
        print("Element not found")

lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
print("The unsorted list is : \n", lst)

key =int(input("Enter the number you want to search in the list : "))
linearSearch(lst,key)
