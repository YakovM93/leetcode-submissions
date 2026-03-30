# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Handle edge cases (empty input)
        if not lists or len(lists) == 0:
            return None
        
        # 2. Divide and Conquer Loop
        while len(lists) > 1:
            mergedLists = []
            
            # Step by 2 to merge pairs (l1 + l2)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Check if l2 exists (handle odd number of lists)
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and add to the new list
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Update lists to the new shrunk version
            lists = mergedLists
            
        return lists[0]

    # Your provided helper function
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next