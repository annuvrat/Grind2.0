nums = [2,1,3,4,6]
k=3


def SumArray(nums,k):

    max_sum = 0

    for  i in range(len(nums)-k+1):

        window  = nums[i:k+i]
        print(window)

        current_sum = sum(window)

        # max_sum= max(current_sum,max_sum)

        if current_sum>max_sum:
            max_sum= current_sum

    return  max_sum



print(SumArray(nums,k))

