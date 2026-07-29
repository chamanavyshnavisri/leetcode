from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c in range(26):
            ch = chr(ord('a') + c)
            half[c] = cnt[ch] // 2
            if cnt[ch] & 1:
                mid = ch

        LIMIT = k

        def ways(freq):
            """number of distinct permutations (capped at LIMIT)"""
            total = sum(freq)
            res = 1
            rem = total
            for f in freq:
                if f == 0:
                    continue
                res *= comb(rem, f)
                if res > LIMIT:
                    return LIMIT
                rem -= f
            return res

        if ways(half) < k:
            return ""

        left = []
        remain = sum(half)

        while remain:
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                w = ways(half)

                if w >= k:
                    left.append(chr(c + ord('a')))
                    remain -= 1
                    break

                k -= w
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]