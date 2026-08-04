class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        res=[]
        for i in range(mini+1,maxi):
            if i not in nums:
                res.append(i)
        return res
        