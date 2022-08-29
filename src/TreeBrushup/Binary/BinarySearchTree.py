from __future__ import annotations
from typing import Any


class Node:
    value: Any
    left: Node
    right: Node

    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None


# TODO: make generic?
class BinarySearchTree:
    root: Node = None

    def __init__(self):
        self.root = None

    def __repr__(self):
        spacing = "     "
        result = ""

        def print_node(n: Node, depth=0):
            if not n.value:
                return

            if n.right:
                print_node(n.right, depth + 1)

            nonlocal result
            result += f"\n{spacing*depth}{n.value}\n"

            if n.left:
                print_node(n.left, depth + 1)

        print_node(self.root)
        return result

    def insert(self, value: Any):
        if not self.root:
            self.root = Node(value)
            return

        def traverse_or_insert(n: Node, value: Any):
            if value == n.value:
                # no duplicates allowed, value is present
                return

            if value < n.value:
                if n.left:
                    traverse_or_insert(n.left, value)
                else:
                    n.left = Node(value)

            if value > n.value:
                if n.right:
                    traverse_or_insert(n.right, value)
                else:
                    n.right = Node(value)

        # if we make it here, traverse until we can insert
        traverse_or_insert(self.root, value)

    def exists(self, value: Any) -> bool:
        def traverse_looking_for(node: Node, value):
            if node is None:
                return False

            if node.value == value:
                return True

            if value < node.value:
                return traverse_looking_for(node.left, value)

            return traverse_looking_for(node.right, value)

        return traverse_looking_for(self.root, value)
