class Solution:
    def minimumPushes(self, word: str) -> int:
        count=0
        n=len(word)
        for i in range(n):
            count+=(i//8)+1
        return count
        