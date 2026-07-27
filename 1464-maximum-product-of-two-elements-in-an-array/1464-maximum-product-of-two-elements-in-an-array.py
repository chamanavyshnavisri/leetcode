class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res1=(nums[-1]-1)*(nums[-2]-1)
        res2=(nums[0]-1)*(nums[1]-1)
        return max(res1,res2)
        