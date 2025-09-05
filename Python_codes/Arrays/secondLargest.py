class Solution:
    def secondLargest(self,nums):
        n=len(nums)
        if n<2:
            return -1
        
        nums.sort()
        