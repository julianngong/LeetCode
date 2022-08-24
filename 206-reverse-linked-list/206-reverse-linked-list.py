# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode=None
        currNode=head
        while currNode != None:
            nextNode=currNode.next
            currNode.next=prevNode
            prevNode=currNode
            currNode=nextNode
        return prevNode
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head==None or head.next==None):
            return(head)
        reverse = self.reverseList(head.next) #basically this reversed list will always return the reversed sublist of the given head node but head.next is still pointing at the first element of the link list passed into reverseList which after reversed list represents the last node element. but we want this last node element to now point to this head as its reversed so this head must be at the back. hence head.next.next (aka the last element of the sublist.next) must be equal to head.
        head.next.next=head
        head.next=None #but now if it finished here then head is the last element so should point to nothing hence
        currentNode=head
        return reverse