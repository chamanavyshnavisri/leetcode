class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []'''
        key={}
        n=len(nums)
        for i in range(n):
            need=target-nums[i]
            if need in key:
                return [i,key[need]]
            else:
                key[nums[i]]=i