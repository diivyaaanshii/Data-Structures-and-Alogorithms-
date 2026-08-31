# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - prev_cp)
                prev_cp = index

            prev = curr
            curr = curr.next
            index += 1

        if min_dist == float('inf'):
            return [-1, -1]

        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]