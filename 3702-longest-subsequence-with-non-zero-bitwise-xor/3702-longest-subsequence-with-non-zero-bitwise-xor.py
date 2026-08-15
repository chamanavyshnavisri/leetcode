class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        '''xor=0
        maxi=0
        left=0
        dup=[0]*len(nums)
        if dup==nums:
            return 0
        for i in range(len(nums)):
            xor^=nums[i]
            right=i+1
            if xor==0:
                right=i
            maxi=max(maxi,right-left)
        return maxi'''
        '''tot=nz=0
        for i in nums:
            nz |= i>0
            tot^=i
        return nz*(len(nums)-(not tot))'''
        total=0
        hasnonzero=False
        for i in nums:
            total^=i
            if i!=0:
                hasnonzero=True
        if not hasnonzero:
            return 0
        if total:
            return len(nums)
        return len(nums)-1

        


        