from typing import List

class Solution:
    def linearSearch(self,nums:List[int],target:int)->int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            

        return -1
    

if __name__=="__main__":
    nums=[1,2,3,4,5]
    target=5
    sol=Solution()
    result=sol.linearSearch(nums,target)
    print(result)
