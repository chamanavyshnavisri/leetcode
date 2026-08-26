class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #brute force
        if len(s)!=len(goal):
            return False
        '''n=len(s)
        for i in range(n):
            rotated=s[i:]+s[:i]
            if rotated==goal:
                return True
        return False'''
        #optimal approach
        double=s+s
        return goal in double

        