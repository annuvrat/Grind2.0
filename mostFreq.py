nums = [1, 2, 2, 3, 2, 4]



def most_freq(nums):

  counts = {}
  max_count = 0
  most_frequent = None

  for num in nums:

    if num not in counts:
      counts[num] = 0

    counts[num] += 1

  for num, count in counts.items():
      if count>max_count:
        max_count = count
        most_frequent = num
  return most_frequent


print(most_freq(nums))  # Output: 2