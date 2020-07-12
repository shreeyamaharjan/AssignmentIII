def insertion_sort(nums):
    for i in range(1, n):
        key_value = nums[i]
        j = i - 1
        while j >= 0 and key_value < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key_value
        print(nums)


lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
print("The unsorted list is : \n", lst)
insertion_sort(lst)
print("The sorted list is : \n", lst)
