class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0  

        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt
                count += 1
                if start == current:
                    break
            start += 1
