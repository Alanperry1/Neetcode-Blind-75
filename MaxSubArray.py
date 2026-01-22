# Time Complexity: O(n) - Single pass through the array with sliding window
# Space Complexity: O(1) - Only using constant extra space
def MaxSubArray(nums,k)
    l,r=0,k-1
    initialSum=sum(nums[l:r+1])
    maxSum=initialSum
    while r<len(nums)-1:
        win_sum=initialSum+nums[r+1]-nums[l]
        l+=1
        r+=1
        initialSum=win_sum
        maxSum=max(win_sum,maxSum)
    return maxSum
