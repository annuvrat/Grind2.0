nums= [1,2,3,4,5,6]
target = 4


def IndexNum(nums,target):
    for num in nums:
        if nums[num] == target:
            return num
        


print(IndexNum(nums,target))