class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums
        v=[]
        k=len(nums)//3
        s={}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for i,j in s.items():
            if j>k:
                v.append(i)
        return v