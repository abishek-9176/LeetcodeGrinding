class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n=float('inf')
        k=0
        for i in range(len(nums)):
            if abs(nums[i]) <= n:
                if k==abs(nums[i]):
                    k=max(nums[i],k)
                else:
                    k=nums[i]
                n=abs(nums[i])
        return k
