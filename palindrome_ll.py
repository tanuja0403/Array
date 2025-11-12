# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next :
            return True 

        fast = head 
        slow = head 

        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

        prev = None 
        curr = slow 
        while curr :
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node 
        second_head = prev 

        first , second = head , second_head
        

        while second :
            if first.val != second.val :
                return False
                break 

            first = first.next 
            second = second.next 
        return True 
            
        

        

        