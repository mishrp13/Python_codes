class Solution:
    def upperHalf(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end=" ")
            for j in range((2*n-2)-2*i):
                print(" ",end=" ")
            for j in range(i+1):
                print("*",end=" ")
            print()

    def lowerHalf(self,n):
        for i in range(1,n):
            for j in range(n-i):
                print("*",end=" ")
            for j in range(2*i):
                print(" ",end=" ")
            for j in range(n-i):
                print("*",end=" ")
            print()

    def Pattern20(self,n):
        self.upperHalf(n)
        self.lowerHalf(n)

if __name__=="__main__":
    N=4
    sol=Solution()
    sol.Pattern20(N)

