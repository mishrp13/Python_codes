
#Brute Force

# from typing import List

# class Solution:
#     def largestElement(self,nums):
#         nums.sort()
#         largest=nums[-1]
#         return largest
    

# if __name__=="__main__":
#     sol=Solution()
#     nums=[12,32,14,82,34,56]
#     largest=sol.largestElement(nums)
#     print(largest)

#optimal approach


from typing import List

class Solution:
    def largestElement(self,nums):
        max=nums[0]

        for num in nums[1:]:
            if num>max:
                max=num

        return max
    

if __name__=="__main__":
    sol=Solution()
    nums=[12,13,21,13]
    ans=sol.largestElement(nums)
    print(ans)