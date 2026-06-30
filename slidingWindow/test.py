nums = [2, 4, 6, 8, 10]

k=3
current_sum=0
max_sum=0
avg_result = []
min_sum = float('inf') 
for i in range(len(nums)- k+1):
    window =  nums[i:i+k]
    print(window)
    current_sum = sum(window)
    average = current_sum/k
    avg_result.append(average)
    max_sum=  max(max_sum,current_sum)
    min_sum = min(min_sum,current_sum,)
    # print(current_sum)
print(max_sum)
print(avg_result)
print(min_sum)
    
