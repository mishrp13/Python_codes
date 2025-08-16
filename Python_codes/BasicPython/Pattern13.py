class Solution:
    def Pattern13(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print(j+1,end=" ")

            for j in range(2*n-2*i):
                print(" ",end=" ")

            for j in range(i,0,-1):
                print(j,end=" ")

            print()

if __name__=="__main__":
    sol=Solution()
    N=4
    sol.Pattern13(N)