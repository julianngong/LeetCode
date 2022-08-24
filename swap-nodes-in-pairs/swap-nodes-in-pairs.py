# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return(head)
        firstnode = head
        secondnode=head.next
        
        firstnode.next=self.swapPairs(secondnode.next)
        secondnode.next=firstnode
        return(secondnode)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return(head)
        firstnode = head
        secondnode = head.next
        thirdnode = head.next.next
        secondnode.next=firstnode
        firstnode.next=self.swapPairs(thirdnode)
        return(secondnode)
        