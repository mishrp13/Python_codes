class Solution:
    def Pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

    def main(self):
        n=5
        sol=Solution()
        sol.Pattern1(n)

if __name__=="__main__":
    Solution().main()



