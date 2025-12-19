class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        
        queue = []
        queue.append (root.left)
        queue.append (root.right)

        while len(queue) > 0:
            left = queue.pop (0)
            right = queue.pop (0)

            if left is None and right is None :
                continue 
            if left is None or right is None :
                return False 
            if left.val != right.val :
                return False 
            
            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True 
            
        