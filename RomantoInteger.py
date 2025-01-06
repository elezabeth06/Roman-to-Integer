class Solution:
    def romanToInt(self, s: str) -> int:
        a = 0
        r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i,j in zip(s,s[1:]):
            if r[i]<r[j]:
                a -= r[i]
            else:
                a += r[i]
        return a + r[s[-1]]
        