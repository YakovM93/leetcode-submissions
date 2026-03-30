class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        number = 0
        number2 = 0
        j = 1
        newlist = ListNode()
        while l1:
            n = l1.val
            n *= j
            j *= 10
            number += n
            l1 = l1.next
        j = 1
        while l2:
            n2 = l2.val
            n2 *= j
            j *= 10
            number2 += n2
            l2 = l2.next
        total = number2 + number
        
        dummy = ListNode(0)
        curr = dummy
        for s in str(total)[::-1]:
            curr.next = ListNode(int(s))
            curr = curr.next
        return dummy.next