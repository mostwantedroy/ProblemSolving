import sys

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node.data, end = '')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end = '')

def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end = '')
    if node.right_node != '.':
        in_order(tree[node.right_node])


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = dict()
    for _ in range(N):
        data, left, right = sys.stdin.readline().split()
        tree[data] = Node(data, left, right)
    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])