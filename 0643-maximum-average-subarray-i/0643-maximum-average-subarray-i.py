class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum=sum(nums[:k])
        maxsum=window_sum
        '''for i in range(n-k+1):
            cursum=0
            for j in range(i,i+k):
                cursum+=nums[j]
            maxsum=max(cursum,maxsum)'''
        for i in range(k,n):
            window_sum=window_sum-nums[i-k]+nums[i]
            maxsum=max(maxsum,window_sum)
        return float(maxsum)/k    