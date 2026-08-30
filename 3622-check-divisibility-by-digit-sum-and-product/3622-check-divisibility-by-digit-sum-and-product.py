class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sumi=0
        prod=1
        while n>0:
            rem=n%10
            sumi+=rem
            prod*=rem
            n=n//10
        return (temp%(sumi+prod)==0)


        