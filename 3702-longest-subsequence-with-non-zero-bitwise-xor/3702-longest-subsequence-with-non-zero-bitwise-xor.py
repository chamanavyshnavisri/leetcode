class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        left=0
        right=0
        xor=0
        maxi=0
        dup=[0]*len(nums)
        if dup==nums:
            return 0
        for i in range(len(nums)):
            xor^=nums[i]
            right=i+1
            if xor==0:
                right=i
            maxi=max(maxi,right-left)
        return maxi


        