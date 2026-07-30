class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length=0
        maxi=0
        st=set(nums)
        for i in st:
            if i-1 not in st:
                cur=i
                length=1
                while length+cur in st:
                    length+=1
                maxi=max(length,maxi)
        return maxi
                

        