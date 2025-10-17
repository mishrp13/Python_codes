class Solution:

    def secondLargest(self,nums):

        n=len(nums)

        if n<2:
            return -1
        
        nums.sort()

        largest = nums[-1]

        secondLargest=-1


        for i in range(n-2,-1,-1):
            if nums[i]!=largest:
                 secondLargest=nums[i]
                 break
           

        return secondLargest

if __name__=="__main__":
    nums=[13,2,1,23,13,43,23]
    sol=Solution()
    ans=sol.secondLargest(nums)
    print("second Largest Element is", ans)

