# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength (head : ListNode) -> int :
            length = 0 
            while head :
                length +=1 
                head = head.next 
            return length 

        lenA = getLength(headA)
        lenB = getLength(headB)

        diff = abs(lenA - lenB)

        if lenA > lenB :
            for _ in range (diff) :
                headA = headA.next 
        else :
            for _ in range (diff) :
                headB = headB.next 

        while headA != headB :
            headA = headA.next 
            headB = headB.next 
                
        return headA

        

        