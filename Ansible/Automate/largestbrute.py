from typing import List

class Solution:

    def LargestElement(self,nums):

        nums.sort()

        largest=nums[-1]

        return largest

if __name__=="__main__":
    nums=[1,3,5,6,856,12]

    sol=Solution()
    largest=sol.LargestElement(nums)
    print("Largest",largest)
