# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            curr =  head
            j = 0
            if not head:
                return None
                
            while curr:
                curr = curr.next
                j += 1
            
            k_temp = j//k
            
            dummy = ListNode(0)
            dummy.next = head
            group_prev = dummy
            
            while k_temp > 0:
                prev = None
                curr = group_prev.next
                for _ in range(k):
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                tail = group_prev.next
                group_prev.next = prev
                tail.next = curr
                group_prev = tail
                k_temp -= 1
                
            return dummy.next

    