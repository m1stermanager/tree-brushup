from TreeBrushup.Binary.BinarySearchTree import BinarySearchTree


def build_bst():
    tree = BinarySearchTree()

    tree.insert(5)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(7)
    tree.insert(9)
    tree.insert(6)
    tree.insert(4)

    return tree


def main():
    tree = build_bst()
    print(tree)


if __name__ == "__main__":
    main()
