class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        s = set()

        for num in arr:
            if 2 * num in s or (num % 2 == 0 and num // 2 in s):
                return True
            s.add(num)

        return False