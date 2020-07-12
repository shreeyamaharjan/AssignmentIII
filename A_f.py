def binarySearch(lst, key):
    l = 0
    u = n - 1

    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == key:
            globals()['pos'] = mid
            return True

        elif key > lst[mid]:
            l = mid + 1

        else:
            u = mid - 1

    return False


lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
lst.sort()
print("The  list is : \n", lst)
key = int(input("Enter the number you wanted to search for : "))
if binarySearch(lst, key):
    print("Key {} found at index {}".format(key, pos))

else:
    print("Key not found")
