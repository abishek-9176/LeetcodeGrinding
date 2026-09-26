class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        k=set(nums)
        a=[]
        v=[]
        c=0
        for i in range(lower,upper+1):
            if i not in k:
                c=1
                if not v:
                    v.append(i)
                b=i
            else:
                if c==1:
                    v.append(b)
                    a.append(v)
                    v=[]
                    c=0
        if len(v)==1:
            v.append(b)
            a.append(v)
        return a

                




