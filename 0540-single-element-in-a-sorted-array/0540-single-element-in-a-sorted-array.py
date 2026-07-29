class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''n=len(nums)
        if n==1:
            return nums[0]
        if nums[1]!=nums[0]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                low=mid+1
            else:
                high=mid-1
        return -1'''
        '''
        brute force

        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            if i==1:
                if nums[i-1]!=nums[i]:
                    return nums[i-1]
            if i==n-1:
                if nums[i-1]!=nums[i]:
                    return nums[i]
            else:
                if nums[i-1]!=nums[i] and nums[i+1]!=nums[i]:
                    return nums[i]
                    
        using bit manipulation:
        ans=0
        for i in nums:
            ans^=i
        return ans'''
        n=len(nums)
        low,high=0,n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:
                high=mid
        return nums[low]