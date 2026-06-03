nums = [1, 1, 2, 2, 3, 4]


def unique_elements(nums):
  result = []
  counts = {}
  for num  in nums:

    if num not in counts:
      counts[num] = 0

    counts[num]+= 1 

  for num, count in counts.items():
      if count == 1:
        result.append(num)


    

   




  return result if result else False



print(unique_elements(nums))