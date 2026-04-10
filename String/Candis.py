class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)   # Step 1
        
        result = []
        
        for c in candies:            # Step 2
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result