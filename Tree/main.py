from binary_tree import *


if __name__ == '__main__':

    # Create Root Node
    root = BinaryTreeNode(100)

    # Create Child Nodes
    root.left = BinaryTreeNode(110)
    root.left.left = BinaryTreeNode(70)
    root.right = BinaryTreeNode(80)

    # Create Leaf Nodes
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(89)

    print("Inorder traversal before insertion:", end=" ")
    list_items_inorder(root)
