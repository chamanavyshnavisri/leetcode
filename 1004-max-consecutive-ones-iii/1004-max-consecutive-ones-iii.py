class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        maxlen=0
        left=0
        for right in range(n):
            if nums[right]==0:
                count+=1
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            curlen=right-left+1
            maxlen=max(curlen,maxlen)
        return maxlen                
        