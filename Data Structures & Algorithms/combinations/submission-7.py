class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(i, n, k, array, result):
            if len(array) == k :
                result.append(list(array))
                return
            if i > n:
                return


            for j in range(i, n+1):
                array.append(j)
                helper(j+1, n, k, array, result)
                array.pop()                
            return 

        helper(1, n, k, [], result)
        return result
        