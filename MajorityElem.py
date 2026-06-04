nums = [2,2,1,1,1,2,2,3,3,3,3,3,3,3
        ]



def majorityElement(nums):
     counts = {}
     for num in nums:
          if num not in counts:
               counts[num] = 0
          
          counts[num]+=1

          print(counts)


     for num,i in counts.items():
          if i > len(nums) // 2:
               return num
           
           


     return False


print(majorityElement(nums))
          
          





# print(majorityElement(nums))
    