# Time Complexity: O(n) - Single pass through the string (filtering and comparing)
# Space Complexity: O(n) - New string stores alphanumeric characters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        for string in s:
            if string.isalnum():
                new+=string
        new=new.lower()
        left,right=0,len(new)-1
        while left<right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True
