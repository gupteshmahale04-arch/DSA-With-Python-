class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        Max = max(candies)
        ans = []

        for i in candies:
            if i + extraCandies >= Max:
                ans.append(True)
            else:
                ans.append(False)

        return ans