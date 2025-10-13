from typing import List
class Solution:
    def LinearSearch(self, nums:List[int], target:int)->int:
        for i in range(len(nums)):
            if (nums[i]==target):
                return i 

        return -1

if __name__=="__main__":
    nums=[1,2,4,5,6,12]
    target=12
    sol=Solution()
    result=sol.LinearSearch(nums,target)
    print(result)