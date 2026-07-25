class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        ind=-1
        i,j=0,n-1
        while i<=j:
            if nums[i]**2>nums[j]**2:
                ans[ind]=nums[i]**2
                ind-=1
                i+=1
            else:
                ans[ind]=nums[j]**2
                ind-=1
                j-=1
        return ans
