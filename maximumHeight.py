class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height (root) :
            if root is not None :
                return 0 
            queue = [root]
            height = 0 

            while len(queue) > 0 :
                levelOfNodes = len(queue)
                height += 1

                count = 0 
                while count < levelOfNodes :
                    currentNode = queue.pop (0)
                    if currentNode.left is not None :
                        queue.append (currentNode.left)
                    if currentNode.right is not None :
                        queue.append (currentNode.right)
                    count += 1
            
            return height
        return height (root)
            

        