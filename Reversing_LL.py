# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n) - Single pass through the linked list
# Space Complexity: O(1) - Only using constant extra space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head

        while curr:
            next_val=curr.next
            curr.next=prev
            prev=curr
            curr=next_val
        return prev
