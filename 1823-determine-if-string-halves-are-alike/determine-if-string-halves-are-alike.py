class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        s=s.lower()
        a=0
        b=0
        c={'a','e','i','o','u'}
        for i in range(n):
            if s[i] in c:
                a+=1
            if s[n+i] in c:
                b+=1
        return a==b