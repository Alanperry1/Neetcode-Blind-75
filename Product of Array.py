# Time Complexity: O(n^2) - Nested loop through array, slicing is O(n)
# Space Complexity: O(n) - Temporary arrays created in slicing
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            temp=nums[:i]+nums[i+1:]
            product.append(math.prod(temp))

        return product
