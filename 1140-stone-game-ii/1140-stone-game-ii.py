class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp=[[[-1]*(2*n) for i in range(2)] for j in range(n)]
        def solve(index,turn,m):
            if index==n:
                return 0
            if dp[index][turn][m]!=-1:
                return dp[index][turn][m]
            if turn:
                res=float('inf')
            else:
                res=float('-inf')
            sm=0
            for i in range(2*m):
                if index+i <n:
                    sm+=piles[index+i]
                    if not turn:
                        res=max(res,sm+solve(index+i+1,turn^1,max(m,i+1)))
                    else:
                        res=min(res,solve(index+i+1,turn^1,max(m,i+1)))
            dp[index][turn][m]=res
            return res
        return solve(0,0,1)        