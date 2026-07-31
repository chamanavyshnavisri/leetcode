# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        dummy = ans 
        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return ans.next
        '''while head and head.val==val:
            head=head.next
        temp=head
        while temp:
            while temp.next and temp.next.val==val:
                temp.next=temp.next.next
            temp=temp.next
        return head'''


            

        