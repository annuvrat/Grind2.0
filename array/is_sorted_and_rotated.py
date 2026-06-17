def check(self, nums):
    n = len(nums)                          # Get array length
    drops = 0                              # Count breaks in order
    
    for i in range(n):                     # Check every element
        # Compare with next (wrap around with %)
        if nums[i] > nums[(i + 1) % n]:   
            drops += 1                     # Found a break
    
    return drops <= 1                      # Valid if ≤ 1 break