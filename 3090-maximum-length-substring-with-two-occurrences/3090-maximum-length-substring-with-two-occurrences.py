class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        freq=[0]*26
        left=0
        ans=0
        for right in range(n):
            index=ord(s[right])-ord('a')
            freq[index]+=1
            while freq[index]>2:
                freq[ord(s[left])-ord('a')]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
