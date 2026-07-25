class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        index=-1
        for i in range(n):
            if nums[i]==0:
                index=i
                break
        if index==-1:
            return
        for j in range(index+1,n):
            if nums[j]!=0:
                nums[index],nums[j]=nums[j],nums[index]
                index+=1


                    