class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def dfs(node):
            if not node:
                return TreeNode(key, val)

            if key < node.key:
                node.left = dfs(node.left)
            elif key > node.key:
                node.right = dfs(node.right)
            else:
                node.val = val
            return node
        
        self.root = dfs(self.root)

    def get(self, key: int) -> int:
        def dfs(node):
            if not node:
                return -1

            if key < node.key:
                return dfs(node.left)
            elif key > node.key:
                return dfs(node.right)
            else:
                return node.val
                
        return dfs(self.root)

    def getMin(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current and current.left:
            current = current.left

        return current.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current and current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        def getMinNode(node):
            current = node

            while current and current.left:
                current = current.left

            return current

        def dfs(node, key):
            if not node:
                return

            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = getMinNode(node.right)
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.key)
            return node

        self.root = dfs(self.root, key)

    def getInorderKeys(self) -> List[int]:
        traversal = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            traversal.append(node.key)
            dfs(node.right)

        dfs(self.root)
        return traversal
