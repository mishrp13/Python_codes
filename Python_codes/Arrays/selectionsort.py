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
    nums=[45,56,12,32,46]
    sol=Solution()
    sorted_list=sol.selectionSort(nums)
    print(f"sorted values of array is : {sorted_list}")


# Here it minimum at the front
# In selection sort, the outer loop goes from 0 to n-2 because the last value
# will already be sorted. The inner loop goes from i+1 to n-1 to find the
# smallest element in the unsorted portion. When we find a smaller value,
# we swap it with the value at index i. 
# Time complexity: O(n^2)
# Space complexity: O(1) (in-place sorting)




