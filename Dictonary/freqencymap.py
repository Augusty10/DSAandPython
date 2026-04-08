nums= [5,6,6,7,2,4,5]
hash_map={}
n=len(nums)
for i in range (0,n):
    hash_map[nums[i]]= hash_map.get(nums[i],0)+1 
    print(hash_map)
    