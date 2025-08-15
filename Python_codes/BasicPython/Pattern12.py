class Solution:
    def Pattern12(self,n):
        for i in range(n):
            for j in range(i+1):
                print(i)
            print()

if __name__=="__main__":
    N=10
    sol=Solution()
    sol.Pattern12(N)