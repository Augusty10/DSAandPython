#Maximum Subarray(kadane Algorithem )

def maxSubArray(nums):
    size = len(nums)
    Current_Sum = 0
    Max_Sum = float('-inf') 

    for i in range(size):
        Current_Sum += nums[i]
        Max_Sum = max(Max_Sum, Current_Sum)
        if Current_Sum < 0:
            Current_Sum = 0
    return Max_Sum
print(maxSubArray([-2, 1, -3,4, -1, 2, 1, -5, 4]))
