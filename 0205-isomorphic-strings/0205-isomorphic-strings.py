class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        mapping={}
        remember=set()
        for i in range(n):
            if s[i] in mapping:
                if mapping[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in remember:
                    return False
            mapping[s[i]]=t[i]
            remember.add(t[i])
        return True
            

        