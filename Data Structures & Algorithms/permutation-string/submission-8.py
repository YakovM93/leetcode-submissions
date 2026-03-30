class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = {}
        cs2 = {}
        leng = 0
        for i in range(len(s1)):
            cs1[s1[i]] = 1 + cs1.get(s1[i], 0)
        l = 0
        for r in range(len(s2)):
            cs2[s2[r]] = 1 + cs2.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                cs2[s2[l]] -= 1
                if cs2[s2[l]] == 0:
                    del cs2[s2[l]]
                l += 1
            if cs2 == cs1:
                return True
        return False