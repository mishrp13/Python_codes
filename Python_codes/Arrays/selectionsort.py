class Solution:
    def selectionSort(self,nums):
        for i in range(len(nums)-1):
            min_index=i

            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_index]:
                    min_index=j

            if min_index!=i:
                nums[i],nums[min_index]=nums[min_index],nums[i]
        
        return nums
    
if __name__=="__main__":
    sol=Solution()
    nums=[64,45,32,43,67]
    sorted_nums=sol.selectionSort(nums)
    print(f"sorted values of array is: {sorted_nums}")

