# Create a node
class BinaryTreeNode:
    def __init__(self, data=None):
        self.key = data
        self.left = None
        self.right = None


# Insert an Item
def insert(root, key):

    if not root:
        root = BinaryTreeNode(key)
        return
    q = []
    q.append(root)

    # perform level order traversal till we find empty place to insert
    while (len(q)):
        root = q[0]
        q.pop(0)

        if (not root.left):
            root.left = BinaryTreeNode(key)
            break
        else:
            q.append(root.left)

        if (not root.right):
            root.right = BinaryTreeNode(key)
            break
        else:
            q.append(root.right)


def list_items_inorder(root):

    if (not root):
        return

    list_items_inorder(root.left)
    print(root.key, end=" ")
    list_items_inorder(root.right)
