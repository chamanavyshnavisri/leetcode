class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=0
        rightmax=0
        left,right=0,n-1
        waterlevel=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    waterlevel+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    waterlevel+=rightmax-height[right]
                right-=1
        return waterlevel
        


        