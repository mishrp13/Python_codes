class Solution:
    def Pattern7(self,n):
        for i in range(n):

            #Printing spaces
            for j in range((n-i)):
                print(" ",end="")

            for j in range(2*i+1):
                print("*", end="")

            for j in range((n-i)):
                print(" ",end="")

            print()

    def main(self):
        N=4
        sol=Solution()
        sol.Pattern7(N)


if __name__=="__main__":
    Solution().main()