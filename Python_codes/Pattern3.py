class Solution:
    def pattern3(self,n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end=" ")
            
            print()

    def main(self):
        N=7
        sol=Solution()
        sol.pattern3(N)

if __name__=="__main__":
    Solution().main()

        