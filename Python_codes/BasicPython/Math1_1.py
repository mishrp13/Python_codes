import math

class Solution:
    def countDigit(self,n):
        if n==0:
            return 1
        count=int(math.log10(n)+1)
        return count
    
n=987
sol=Solution()
print(sol.countDigit(n))