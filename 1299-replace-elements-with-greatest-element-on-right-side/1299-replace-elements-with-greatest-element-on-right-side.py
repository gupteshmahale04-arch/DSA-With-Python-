class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, temp)

        return arr