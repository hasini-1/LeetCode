# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        result = ""
        while head:
            result += str(head.val)
            head = head.next
        return int(result,2)
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        