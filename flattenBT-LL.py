class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.next = None 

        def solve(node):
            if node is None :
                return 

            solve(node.right)
            solve(node.left)

            node.left = None 
            node.right = self.next
            self.next = node 
        solve(root)