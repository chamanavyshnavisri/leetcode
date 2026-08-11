class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        hash_set=set(nums)
        sumi=nums[0]
        for i in range(1,n):
            if nums[i]==nums[i-1] +1:
                sumi+=nums[i]
            else:
                break
        while sumi in hash_set:
            sumi+=1
        return sumi

        