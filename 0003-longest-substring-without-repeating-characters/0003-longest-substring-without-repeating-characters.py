class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxlen=0
        left=0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[end])
            maxlen=max(maxlen,end-left+1)

        return maxlen
        