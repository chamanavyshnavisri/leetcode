class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxi=0
        i,j=0,n-1
        while i<n and j>=0:
            hei=min(height[i],height[j])
            wid=j-i
            area=wid*hei
            maxi=max(maxi,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1  
        return maxi


        