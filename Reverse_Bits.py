# Time Complexity: O(1) - Fixed 32 iterations
# Space Complexity: O(1) - Only using constant extra space
class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            last_dig=n&1
            result=(result<<1)|last_dig
            n>>=1

        return result
