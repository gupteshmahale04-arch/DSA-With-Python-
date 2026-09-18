class Solution:
    def countSegments(self, s: str) -> int:
        # count=1
        # for i in s:
        #     if i is" " :
        #         count+=1
        # return count

        return len(s.split())