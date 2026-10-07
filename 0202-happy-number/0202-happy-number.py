class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)
        return n == 1
