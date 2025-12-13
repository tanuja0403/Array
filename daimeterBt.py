class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0 
        def height (root):
            if not root :
                return 0 
            left = height (root.left)
            right = height (root.right)
            self.daimeter = max (self.diameter , left + right)
            return 1 + max (left , right)
        height (root)   
        return self.diameter