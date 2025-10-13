from typing import List

class Solution:

    def Largest(self,nums):

        max_val=nums[0]

        for num in nums[1:]:

            if num > max_val:
                max_val=num

        return max_val


if __name__=="__main__":
    nums=[1,2,34,4,12]
    sol=Solution()
    result=sol.Largest(nums)
    print(result)
