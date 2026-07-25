class Solution:
    def maxProduct(self, n: int) -> int:
        nums=[]
        while n>0:
            nums.append(n%10)
            n=n//10
        m=len(nums)
        maxi=0
        cur=0
        for i in range(m):
            for j in range(i+1,m):
                cur=nums[i]*nums[j]
                maxi=max(maxi,cur)
        return maxi
        
        