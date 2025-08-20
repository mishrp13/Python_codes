from typing import List

class Solution:
    def largestElement(self,nums):
        nums.sort()
        largest=nums[-1]
        return largest
    

if __name__=="__main__":
    sol=Solution()
    nums=[12,32,14,82,34,56]
    largest=sol.largestElement(nums)
    print(largest)