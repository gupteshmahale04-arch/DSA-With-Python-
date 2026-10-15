class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1.0

            half = pow(x, n // 2)

            if n % 2 == 0:
                return half * half

            return half * half * x

        if n < 0:
            return 1 / pow(x, -n)

        return pow(x, n)