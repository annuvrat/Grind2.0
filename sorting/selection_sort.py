nums = [64, 25, 12, 22, 11]


def selectionSort(nums):

    n = len(nums)


    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if nums[min_index] > nums[j]:
                min_index = j

        
        nums[i],nums[min_index] = nums[min_index],nums[i]


    return nums

      
print(selectionSort(nums))