# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        if head and head.val == val:
            head = head.next
        if current and current.val == val:
            current = current.next
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        while head and head.val == val:
            head = head.next
        return head