class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count=0
        rem1=0
        rem2=0
        for i in stones:
            if i%3==0:
                count+=1
            if i%3==1:
                rem1+=1
            if i%3==2:
                rem2+=1
        if rem1==0 and rem2==0:
            return False
        if count%2==0:
            return rem1>0 and rem2>0
        return abs(rem1-rem2) >2

