class Solution:
    def pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")

            print()

    def main(self):
        N=5
        sol=Solution()
        sol.pattern2(N)

if __name__=="__main__":
    Solution().main()

