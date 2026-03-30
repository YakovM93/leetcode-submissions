class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        currp = p
        currq = q
        stakq = []
        stakp = []

        while (currp or currq) or (stakp or stakq):
            if not currq or not currp:
                if currp != currq:
                    return False

            if currp and currq:
                if currp.val == currq.val:
                        stakq.append(currq)
                        stakp.append(currp)
                        currp = currp.left
                        currq = currq.left
                else :
                    return False

            else:
                currp = stakp.pop()
                currq = stakq.pop()
                currp = currp.right
                currq = currq.right


        return True