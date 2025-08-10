class Solution:
    def Pattern4(self,n):
        for i in range(n):
            for j in range(i+1):
                print(i+1,end=" ")
            
            print()

    def main(self):
        N=7
        sol=Solution()
        sol.Pattern4(N)


if __name__=="__main__":
    Solution().main()
