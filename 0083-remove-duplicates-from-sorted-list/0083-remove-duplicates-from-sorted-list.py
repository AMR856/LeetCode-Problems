# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set_number = set()
        current = head
        while current and current.next:
            set_number.add(current.val)
            if current.next.val in set_number:
                current.next = current.next.next
            else:
                current = current.next
        return head