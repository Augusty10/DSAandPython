
from collections import defaultdict

def subarray_sum(nums, k):
    count =0
    prefix=0
    freq = defaultdict(int)
    freq[0]=1   #empty prefix 

    for x  in nums:
        prefix+=x
        count += freq[prefix-k]
        freq[prefix]+=1
        return count 
    print(subarray_sum([1,1,1],2))

 
#Time Complexity: O(n)
#Space Complexity: O(n)
