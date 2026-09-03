class Solution:
    def maximumSwap(self, num: int) -> int:
        k=list(map(int,str(num)))
        v=sorted(k,reverse=True)
        d=[]
        
        for i in range(len(k)):
            if k[i]!=v[i]:
                for j in range(i+1,len(k)):
                    if k[j]==v[i]:
                        d.append(j)
                j=d[-1]
                k[i],k[j]=k[j],k[i]
                break
        return int(''.join(map(str, k)))
