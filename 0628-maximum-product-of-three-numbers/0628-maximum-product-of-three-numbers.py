class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        popro=nums[-1]*nums[-2]*nums[-3]
        smpro=nums[0]*nums[1]*nums[-1]
        maxi=max(popro,smpro)
        return maxi


        