nums = [11,7,15,2]
target = 9

def twoSum(nums,target):
    counts = {}
    for i, num in enumerate(nums):  
        needed = target - num
        if needed in counts:
            return [counts[needed], i]
        counts[num] = i
    return False
      
print(twoSum(nums,target))
 