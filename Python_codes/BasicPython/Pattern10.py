class Solution:
    def Pattern1(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()

    def Pattern2(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*", end=" ")
            print()

    def Pattern10(self,n):
        self.Pattern1(n)
        self.Pattern2(n-1)

if __name__=="__main__":
    N=7
    sol=Solution()
    sol.Pattern10(N)






    