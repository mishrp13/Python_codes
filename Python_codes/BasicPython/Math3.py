class Solution:
    def reverseNumbers(self,n):
        reverseNumber=0
        while(n>0):
            lastDigit=n%10
            reverseNumber=reverseNumber*10+lastDigit
            n=n//10
        return reverseNumber

if __name__=="__main__":
    n=int(input("Enter a number: "))
    sol=Solution()
    ans=sol.reverseNumbers(n)
    print(f"Revere number of given number is:{ans}")
