class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            v=min(nums)
            for j in range(len(nums)):
                if nums[j]==v:
                    nums[j]*=multiplier
                    break
        return nums
                