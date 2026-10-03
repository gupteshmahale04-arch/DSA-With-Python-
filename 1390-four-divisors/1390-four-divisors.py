class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def divisors(n):
            divs = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.append(i)
                    if i != n // i:  
                        divs.append(n // i)
            return divs
        
        total = 0
        for num in nums:
            divs = divisors(num)
            if len(divs) == 4:  
                total += sum(divs)
        return total

