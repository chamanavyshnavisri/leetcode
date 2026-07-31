# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        ans=length-n
        if not ans:
            return head.next
        temp=head
        for i in range(ans-1):
            temp=temp.next
        temp.next=temp.next.next
        return head

        