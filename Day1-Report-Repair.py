'''The Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
'''

# Sum of two items in a list equal to a total

def find_product_of_two(arr,total):
  s = set()
  for each in arr:
    tmp = total - each
    if tmp in s:
      print(tmp * each)
    s.add(tmp)
    
'''
The three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

'''

# Sum of three items in a list equal to a total
    
def find_product_of_triplets(arr,total):
  for i in range(0, len(arr)-1): 
      # Find pair in subarray A[i + 1..n-1]  
      # with sum equal to sum - A[i] 
      s = set() 
      curr_sum = total - arr[i] 
      for j in range(i + 1, len(arr)): 
          if (curr_sum - arr[j]) in s: 
              print((curr_sum-arr[j]) * arr[i] * arr[j])
          s.add(arr[j])
