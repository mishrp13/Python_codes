class Solution:
    def Pattern13(self,n):
        num=1
        for i in range(n+1):
            for j in range(i):
                print(num,end=" ")
                num=num+1
            print()



if __name__=="__main__":
    N=5
    sol=Solution()
    sol.Pattern13(N)