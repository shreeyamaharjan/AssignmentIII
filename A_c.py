def partition(nums, low, high):
    i = (low - 1)
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return (i + 1)


# sort
def quickSort(nums, low, high):
    if low < high:
        part = partition(nums, low, high)
        quickSort(nums, low, part - 1)
        quickSort(nums, part + 1, high)


lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
print("The unsorted list is : \n", lst)
quickSort(lst, 0, n - 1)
print("The sorted list is : \n")
for i in range(n):
    print(lst[i], end=" ")
