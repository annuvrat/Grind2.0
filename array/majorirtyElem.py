nums = [1,2,3,4,4,4,4]

def majorityElement(nums):
      counts = {}

      for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num]+=1

      for count,i in counts.items():
          if i > len(nums)/2:
              return count
          
    
      return 0


print(majorityElement(nums))
        