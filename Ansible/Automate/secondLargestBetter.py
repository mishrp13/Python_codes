class Solution:

    def secondLargest(self,nums):

        n=len(nums)
        if n<2:
            return -1

        largest=float('-inf')
        secondLargest=float('-inf')

        for i in range(n):
            largest=max(largest,nums[i])


        for i in range(n):
            if nums[i]>secondLargest and nums[i]!=largest:
                secondLargest=nums[i]


        return -1 if secondLargest == float('-inf') else secondLargest



if __name__=="__main__":
    nums=[12,12,32,12,43,534]
    sol=Solution()
    ans=sol.secondLargest(nums)
    print(ans)


