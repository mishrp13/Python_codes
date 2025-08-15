class Solution:
    def countOddDigit(self,n):
        countOdd=0
        while(n>0):
            lastDigit=n%10
            if lastDigit%2==1:
                countOdd=countOdd+1
            n=n//10
        return countOdd
    
n=678393333
sol=Solution()
print(sol.countOddDigit(n))
    
            
     

       
