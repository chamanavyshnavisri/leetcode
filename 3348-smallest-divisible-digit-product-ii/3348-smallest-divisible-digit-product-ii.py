class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def build_end(req, size):
            res = []

            # Factorize the remaining requirement
            # using digits from 9 down to 2.
            for f in range(9, 1, -1):
                while req % f == 0:
                    req //= f
                    res.append(str(f))

            # Pad with 1's to obtain the desired length.
            if len(res) < size:
                res += ['1'] * (size - len(res))

            return "".join(res[::-1])

        n = len(num)

        # Check that t only contains valid prime factors.
        curr = t
        for f in [2, 3, 5, 7]:
            while curr % f == 0:
                curr //= f

        if curr != 1:
            return "-1"

        # rem[i] = remaining factor needed after
        # processing the first i digits.
        rem = [0] * (n + 1)
        rem[0] = t

        for i in range(n):
            if num[i] == '0':
                break
            rem[i + 1] = rem[i] // gcd(rem[i], int(num[i]))

        # The original number already satisfies the condition.
        if rem[-1] == 1:
            return num

        z = num.find('0')
        start = z if z != -1 else n - 1

        # Try increasing one digit from right to left.
        for i in range(start, -1, -1):
            end_size = n - i - 1

            for d in range(int(num[i]) + 1, 10):
                last = build_end(
                    rem[i] // gcd(rem[i], d),
                    end_size
                )

                if len(last) == end_size:
                    return num[:i] + str(d) + last

        # No solution of the same length exists.
        return build_end(t, n + 1)


