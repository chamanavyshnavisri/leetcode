class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        r=1
        left=0
        freq={}
        for right in range(n):
            freq[nums[right]]=freq.get(nums[right],0)+1
            while freq[nums[right]]>k:
                d=nums[left]
                freq[d]-=1
                left+=1
            r=max(r,right-left+1)
        return r