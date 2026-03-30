class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dici = defaultdict(list)
        for s in strs :
            otiot  = [0]*26
            for c in s:
                otiot[ord(c)-ord("a")] += 1
            dici[tuple(otiot)].append(s)    

        return list(dici.values())
