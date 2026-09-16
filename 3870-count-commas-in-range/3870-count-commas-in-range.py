class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        temp=n
        count=0
        while temp:
            count+=1
            temp=temp-1
            if temp<1000:
                return count
        