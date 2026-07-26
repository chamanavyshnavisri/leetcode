class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        res1=nums[-1]*nums[-2]*nums[-3]
        res2=nums[0]*nums[1]*nums[-1]
        maxi=max(res1,res2)
        return maxi


        