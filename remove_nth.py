class ListNode :
    def __init__ (self , val = 0 , next = None):
        self.val = val 
        self.next = next

class Solution :
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head 
        pointer = head
        length = 0 
        counter = 0 

        while temp :
            length += 1 
            temp = temp.next 

        if n == length :
            return head.next
        
        for _ in range (length - n - 1):
            pointer = pointer.next 
        pointer.next = pointer.next.next 
        return next 