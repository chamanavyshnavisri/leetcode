class Solution:
    def minimumPushes(self, word: str) -> int:
       push=0
       arr=Counter(word)
       for i,x in enumerate(sorted(arr.values(),reverse=True)):
            push+=(i//8 + 1)*x
       return push

       

        