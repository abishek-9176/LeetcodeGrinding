class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(i%2==0 for i in nums1):
            return True
        if min(nums1)%2==1:
            return True
        return False