class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        Left,Right=0,len(numbers)-1
        while Left<Right:
            Find=numbers[Left]+numbers[Right]
            if Find==target:
                return [Left+1,Right+1]
            elif Find<target:
                Left+=1
            else:
                Right-=1
   


            

        