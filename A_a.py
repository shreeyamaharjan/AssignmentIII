def bubble_sort(nums):
    for i in range(n - 1):
        for j in range((n - 1) - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                print(nums)

            else:
                print(nums)
        print("\n")


lst = []
n = int(input("Enter the size of the list : "))
for i in range(n):
    x = int(input())
    lst.append(x)
print("The unsorted list is : ", lst)
bubble_sort(lst)
print("The sorted list is : \n", lst)
