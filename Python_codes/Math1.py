class Solution:
    def countDigit(self,n):
        if n==0:
            return 1
        
        cnt=0
        while(n>0):
            cnt=cnt+1
            n=n//10

        return cnt
    
n=7896
sol=Solution()
print(sol.countDigit(n))