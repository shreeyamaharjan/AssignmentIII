def mergeSort(nums):
    if n > 1:
        mid = n // 2
        left_list = nums[:mid]
        right_list = nums[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                nums[k] = left_list[i]
                i += 1
                k += 1
            else:
                nums[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            nums[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            nums[k] = right_list[j]
            j += 1
            k += 1


lst = []
n = int(int(input("Enter the size of the list : ")))
for i in range(n):
    x = int(input())
    lst.append(x)
print("The unsorted list is : \n", lst)
mergeSort(lst)
print("The sorted list is :\n ", lst)
