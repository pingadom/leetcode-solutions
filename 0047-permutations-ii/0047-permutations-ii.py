class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = set()
        l = len(nums)

        def backtrack(i):
            print(nums,i)
            if i == l:
                #print('append')
                res.add(tuple(nums))
                #print(res)
                return

            for j in range(i,l):
                nums[i],nums[j] = nums[j],nums[i]
                backtrack(i+1)
                nums[j],nums[i] = nums[i],nums[j]
        
        backtrack(0)
        return list(map(list, list(res)))
        