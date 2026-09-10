class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num=str(num)
        if len(num)==1 and num[0]=='0':
            return True
        if num[-1]=='0':
            return False
        return True