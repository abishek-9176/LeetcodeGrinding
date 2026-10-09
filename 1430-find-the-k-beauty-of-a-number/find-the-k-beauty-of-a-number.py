class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        if k==1:
            num=str(num)
            c=0
            for i in range(len(num)):
                v=num[i]
                if v!='0' and int(num)%int(v)==0:
                    c+=1
            return c
        else:    
            num=str(num)
            c=0
            for i in range(len(num)):
                v=num[i]
                for j in range(i+1,len(num)):
                    v+=num[j]
                    if len(v)==k:
                        if v.count('0')==k:
                            break
                        if int(num)%int(v)==0:
                            c+=1
                            break
            return c


            