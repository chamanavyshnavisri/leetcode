# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addnodes(a,b):
        grater=False
        if a+b<10:
            return a+b
        else:
            return (a+b)%10


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        temp=dummy
        total=carry=0
        while l1 or l2 or carry:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            num=total%10
            carry=total//10
            dummy.next=ListNode(num)
            dummy=dummy.next
        return temp.next
            
        