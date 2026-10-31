class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        End=len(hours)-1
        for i in range (len(hours)//2):
            if hours[i]>=target:
                count+=1
            if hours[End-i]>=target:
                count+=1

        if len(hours)%2!=0 and hours[len(hours)//2]>=target:
            count+=1

        return count