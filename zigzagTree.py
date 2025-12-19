class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        
        result = []
        queue = [root]
        left_right = True 


        while queue :
            level_size = len(queue)
            current_level = []
            stack = []

            count = 0 

            while count < level_size:
                node = queue.pop (0)

                if left_right :
                    current_level.append (node.val)
                else :
                    stack.append (node.val)

                if node.left :
                    queue.append (node.left)
                if node.right :
                    queue.append (node.right)

                count += 1

            while stack :
                current_level.append (stack.pop())
            result.append (current_level)
            left_right = not left_right
        return result





    

