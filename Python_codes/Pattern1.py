
class Solution:

    def patten1(self,n):

        for i in range(n):
            for j in range(n):
                print("-",end=" ")
            print()

    def main(self):
        N=5
        sol=Solution()
        sol.patten1(N)

if __name__=="__main__":
    Solution().main()

