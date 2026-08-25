class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first,last=strs[0],strs[-1]
        n=min(len(first),len(last))
        ans=[]
        for i in range(n):
            if first[i]!=last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)
        