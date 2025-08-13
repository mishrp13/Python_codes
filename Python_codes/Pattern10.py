class Solution:
    def Pattern8(self,n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            for j in range(n-i):
                print(" ",end=" ")

            print()

    def Pattern9(self,n):
        for i in range(1,n):
            for j in range(i+1):
                print(" ",end=" ")
            for j in range((2*n-1)-(2*i)):
                print("*",end=" ")
            for j in range(i+1):
                print(" ",end=" ")
            
            print()

    def Pattern10(self,n):
        self.Pattern8(n)
        self.Pattern9(n)


if __name__=="__main__":
    sol=Solution()
    sol.Pattern10(7)