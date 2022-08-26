# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        if list1==None and list2==None:
            result=None
        elif list1==None:
            result=list2
        elif list2==None:
            result=list1
        elif list1.val<list2.val:
            result.val=list1.val
            result.next=self.mergeTwoLists(list1.next,list2)
        elif list1.val>=list2.val:
            result.val=list2.val
            result.next=self.mergeTwoLists(list1,list2.next)
        print(result)
        return(result)
