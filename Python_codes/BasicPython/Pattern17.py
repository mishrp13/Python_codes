class Solution:
    def Pattern17(self,n):
        for i in range(n+1):
            for j in range(n-i):
                print(" ",end=" ")

            ch=chr(ord('A'))

            for j in range(2*i-1):
                print(ch,end=" ")
                if j<i-1:
                    ch=chr(ord(ch)+1)
                else:
                    ch=chr(ord(ch)-1)


            for j in range(n-i):
                print(" ",end=" ")

            print()

if __name__=="__main__":
    N=5
    sol=Solution()
    sol.Pattern17(N)
