class Solution:
    def Pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()


    def main(self):
        sol=Solution()
        N=5
        ans=sol.Pattern2(N)

if __name__=="__main__":
    Solution().main()