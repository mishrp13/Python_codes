class Solution:
    def Pattern16(self,n):
        for i in range(n+1):
            ch=chr(ord('A')+i)
            for j in range(i+1):
                print(ch,end=" ")
            print()
            


if __name__=="__main__":
    N=6
    sol=Solution()
    sol.Pattern16(N)