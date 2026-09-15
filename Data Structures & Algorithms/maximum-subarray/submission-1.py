class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub,cursum=nums[0],0
        for num in nums:
            if cursum < 0:
                cursum=0
            cursum += num
            maxsub = max(maxsub,cursum)
        return maxsub