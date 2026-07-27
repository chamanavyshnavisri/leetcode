class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=0
        sumi=0
        minlen=float('inf')
        for right in range(n):
            sumi+=nums[right]
            while sumi>=target:
                minlen=min(minlen,right-left+1)
                sumi-=nums[left]
                left+=1

        if minlen==float('inf'):
            return 0
        return minlen
        
