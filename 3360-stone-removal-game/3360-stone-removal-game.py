class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice=True
        moves=10
        while n-moves>=0:
            n-=moves
            moves-=1
            alice=not alice
        return not alice