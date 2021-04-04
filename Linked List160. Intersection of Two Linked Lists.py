# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA=headA
        curB=headB
        while curA!=curB:
            if curA is None and curB is not None:
                curA=headB
                curB=curB.next
            elif curB is None and curA is not None:
                curB=headA
                curA=curA.next
            elif curB is not None and curA is not None:
                curA=curA.next
                curB=curB.next
        
        return curA
            
