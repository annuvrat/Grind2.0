nums = [2,1,3,4,6]

k=2
current_sum=0
max_sum=0
x=7
X_window=[]
max_window =[]
avg_result = []
min_sum = float('inf')

def function(nums,x,max_window,max_sum):

 for i in range(len(nums)- k+1):
    window =  nums[i:i+k]
    print(window)
    current_sum = sum(window)
    if current_sum>max_sum:
        max_sum=current_sum
        max_window = window

    if current_sum>x:
        X_window= window
        print(X_window)
        return X_window
    # average = current_sum/k   
    # avg_result.append(average)
    # max_sum=  max(max_sum,current_sum)
    # max_window= nums[i:i+k]
    # min_sum = min(min_sum,current_sum,)
    # print(current_sum)
# print(max_sum)
# print(avg_result)
# print(min_sum)



function(nums,x,max_window,max_sum)
