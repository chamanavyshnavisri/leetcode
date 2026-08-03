class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        st1,st2=[],[]
        for i in s:
            if i=='#':
                if not st1:
                    continue
                st1.pop()
            else:
                st1.append(i)
        for i in t:
            if i=='#':
                if not st2:
                    continue
                st2.pop()
            else:
                st2.append(i)
        return st1==st2
            
        