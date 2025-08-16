class Solution:
    def Pattern15(self,n):
        for i in range(n+1):
            for ch in range(ord('A'),ord('A')+n-i):
                print(chr(ch),end=" ")
            print()


if __name__=="__main__":
    N=24
    sol=Solution()
    sol.Pattern15(N)