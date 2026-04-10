class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    if p_copy not in new_perms:
                        new_perms.append(p_copy)
                   # if i < len(p) and p[i] == n: break
            perms = new_perms

        return perms