class Solution:
    def Pattern5(Self,n):
        for i in range(n):
            for j in range(n-i):
                print("*", end=" ")
            print()

    def main(self):
        N=7
        Sol=Solution()
        Sol.Pattern5(N)


if __name__=="__main__":
    Solution().main()
