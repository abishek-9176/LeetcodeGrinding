class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ms=nums[0]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s>ms:
                ms=s
            if s<0:
                s=0
        return ms 
