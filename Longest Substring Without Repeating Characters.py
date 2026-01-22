# Time Complexity: O(n) - Sliding window with two pointers
# Space Complexity: O(min(n, m)) - Set stores unique characters, m is charset size
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        result=0
        l=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            result=max(result,r-l+1)

        return result
