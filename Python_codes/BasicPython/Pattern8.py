class Solution:
    def Pattern8(self,n):
        for i in range(0,n):
            for j in range(0,i):
                print(" ",end=" ")

            for j in range(0,(2*n-1)-(2*i)):
                print("*",end=" ")

            for j in range(0,i):
                print(" ",end=" ")


            print()

    def main(self):
        N=7
        sol=Solution()
        sol.Pattern8(N)


if __name__=="__main__":
    Solution().main()