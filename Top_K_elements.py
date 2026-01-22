# Time Complexity: O(n log n) - O(n) to count frequencies + O(n log n) to sort
# Space Complexity: O(n) - Hash map stores unique elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        sorted_keys = sorted(seen, key=lambda x: seen[x])

        return sorted_keys[::-1][:k]
