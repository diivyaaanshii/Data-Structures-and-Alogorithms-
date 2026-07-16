# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        cycle_exists=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                cycle_exists=True
                break
        if not cycle_exists:
            return None
        ptr=head
        while ptr!=fast:
            ptr=ptr.next
            fast=fast.next
        return ptr