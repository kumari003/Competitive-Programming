# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def removeNode (head):
            if (head == None):
                return None
            head.next = removeNode(head.next);
            return head.next if (head.next != None and head.val < head.next.val) else head;
        return removeNode(head)  
