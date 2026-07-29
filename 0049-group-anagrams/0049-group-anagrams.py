class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        fin={}
        for i in strs:
            k="".join(sorted(i))
            if k not in fin:
                fin[k]=[]
            fin[k].append(i)
        return list(fin.values())

        