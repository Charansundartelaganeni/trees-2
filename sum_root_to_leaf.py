#TC:O(n) 
#SC:O(h)
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int: 

        self.result = 0 
        self.inorderTraversal(root,0) #pass the root into recursion
        return self.result 

    def inorderTraversal(self, root, currsum): 

        if root == None: #base condition
            return  

        self.inorderTraversal(root.left, currsum*10+root.val)  #traverse on left roots with incrementing currentsum by lifting the number down to the top

        if root.left == None and root.right == None: #when recursion unfolds, append the value to the result
            self.result += currsum*10+root.val

        self.inorderTraversal(root.right,currsum*10+root.val) ##traverse on right roots with incrementing currentsum by lifting the number down to the top