class Solution:
    def minimumPushes(self, word: str) -> int:
        push=0
        arr=sorted(Counter(word).values(),reverse=True)
        n=len(arr)
        for i in range(n):
            push+=arr[i]*(i//8 + 1)
        return push

        