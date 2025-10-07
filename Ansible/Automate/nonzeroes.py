from typing import List

class Solution:
    def moveZeroes(self, nums: List[int])->None:
        n=len(nums)

        temp=[0]*n
        count=0

        for i in range(n):
            if(nums[i]!=0):
                temp[count]=nums[i]
                count+=1


        for i in range(count):
            nums[i]=temp[i]

        for i in range(count,n):
            nums[i]=0

if __name__=="__main__":
    nums=[1,0,3,0,4,5,6]
    sol=Solution()
    sol.moveZeroes(nums)
    print("Array after moving zeroes to end: ",nums)