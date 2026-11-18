class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left,right = 0,len(numbers)-1
        total=(numbers[left] + numbers[right])
        while total != target:
            if total > target:
                right -= 1
            else:
                left += 1
            total=(numbers[left] + numbers[right]) 

        return [left+1,right+1] 
        