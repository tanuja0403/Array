class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or root.left:
            return root 
        
        queue= []
        front = 0 

        queue.append (root)
        queue.append(None)

        while front < len(queue):
            curr = queue[front]
            front += 1

            if curr is None :
                if front >= len(queue):
                    break 
                prev = None 
                queue.append (None)
                continue 
            
            if prev is not None :
                prev.next = curr
            prev = curr 

            if curr.left is not None :
                queue.append(curr.left)
            if curr.right is not None :
                queue.append(curr.right)

        return root 

        
        