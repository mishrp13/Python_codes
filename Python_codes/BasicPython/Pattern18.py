class Solution:
    def Pattern18(self,n):
         el=ord('A')+n-1
         for i in range(n):
              for ch in range(el-i,el+1):
                   print(chr(ch),end=" ")
              print()

#
if __name__=="__main__":
     N=5
     sol=Solution()
     sol.Pattern18(N)
             
