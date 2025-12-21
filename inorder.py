
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder (root):
            if root is None:
                return []
            left = inorder(root.left)
            right = inorder(root.right)
            return left + [root.val] + right
        return inorder(root)
