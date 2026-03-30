
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack  = []

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        node = self.stack.pop()
        self.cur = node.right
        return node.val

    def hasNext(self) -> bool:
        if  self.stack or self.cur:
            return True
        else:
            return False
