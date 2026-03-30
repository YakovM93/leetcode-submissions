class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sort_num = nums
        res = []
        for i in range(len(sort_num)):
            if i > 0 and sort_num[i] == sort_num[i-1]:
                continue

            l,r = i + 1,len(sort_num)-1
            while l < r:
                tsum = sort_num[i]+ sort_num[l] +sort_num[r]
                if tsum > 0:
                    r-=1
                elif tsum < 0:
                    l+=1
                else:
                    res.append([sort_num[i], sort_num[l],sort_num[r]])
                    l += 1
                    while l < r and sort_num[l] == sort_num[l-1]:
                        l+=1
        return res