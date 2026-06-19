nums=[0,1,0,3,12]
def moveZeroes(nums):
    
    n= len(nums)
    left =0
    right =n-1
    while left<right:

        if nums[left] ==0 and nums[right]!=0:
            nums[left],nums[right] = nums[right],nums[left]


            left+=1
            right-=1
        elif nums[left] != 0:
         left += 1
            
        # Case 3: Right is zero -> It's in correct relative spot (at end), move right backward
        elif nums[right] == 0:
         right -= 1
        
    return nums


        


print(moveZeroes(nums))