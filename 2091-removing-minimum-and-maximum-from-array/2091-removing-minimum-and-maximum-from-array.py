class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        minidx=nums.index(min(nums))
        maxidx=nums.index(max(nums))
        right=max(minidx,maxidx)
        left=min(minidx,maxidx)
        front=right+1
        back=n-left
        total=left+1+n-right
        return min(front,back,total)
        
        