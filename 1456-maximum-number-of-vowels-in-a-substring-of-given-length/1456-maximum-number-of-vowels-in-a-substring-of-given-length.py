class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        vowel='aeiou'
        for i in range(k):
            if s[i] in vowel:
                count+=1
        maxi=count
        for j in range(k,n):
            if s[j-k] in vowel:
                count-=1
            if s[j] in vowel:
                count+=1
            maxi=max(maxi,count)
        return maxi
            
        