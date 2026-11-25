class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        pre_p = [nums[0]]
        post_p = [nums[-1]]
        t = 1
        for i in range(1,len(nums)):
            pre_p.append(pre_p[-1]*nums[i])
            post_p.append(post_p[-1]*nums[len(nums)-1-i])
        print(pre_p,post_p)
        res[0],res[-1] = post_p[-2],pre_p[-2]
        print(res)
        for j in range(1,len(nums)-1):
            res[j] = pre_p[j-1] * post_p[len(nums)-2-j]

        
        return res
                
                