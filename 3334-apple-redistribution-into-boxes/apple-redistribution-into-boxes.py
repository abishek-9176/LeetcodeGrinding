class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        k=sum(apple)
        c=0
        capacity.sort()
        v=0
        for i in range(len(capacity)-1,-1,-1):
            v+=capacity[i]
            c+=1
            if v>=k:
                return c
