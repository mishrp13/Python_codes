class Solution:
    def Pattern14(self,n):
        for i in range(n+1):
            for ch in range(ord('A'),ord('A')+i+1):
                print(chr(ch),end=" ")
            print()


if __name__=="__main__":
    N=4
    sol=Solution()
    sol.Pattern14(N)
