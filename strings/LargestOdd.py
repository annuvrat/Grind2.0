num="1243564567"

def largestOddNumber(num):
    n=len(num)
    for i in range(n-1,-1,-1):
        # print(num[i])
        if int(num[i])%2 != 0:
            return num[:i+1]

    return False


print(largestOddNumber(num))