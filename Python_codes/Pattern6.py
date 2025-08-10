class Solution:
    def Pattern6(self,n):
        for i in range(n):
            for j in range(n-i):
                print(j+1,end="")

            print()

    def main(self):
        N=5
        sol=Solution()
        sol.Pattern6(N)


if __name__=="__main__":
    Solution().main()