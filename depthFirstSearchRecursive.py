import timeit
class Node:
    def __init__(self, value, children=None):
        # a leaf node has an empty list of children
        if children is None:
            children = []
        self.value = value
        self.children = children

root = Node(1, [
    Node(2, [
        Node(3, [
            Node(4),
            Node(5)
        ]),
        Node(6)
    ]),
    Node(7, [
        Node(8, [
            Node(9)
        ])
    ]),
    Node(10)
])

def depth_first_search(node, target):
    # check the root node first
    if node.value == target:
        return node
    
    # search recursively in the child subtrees
    for child in node.children:
        found = depth_first_search(child, target)
        if found:
            # "go home early"
            return found
    
    # "go home late", target wasn't found
    return None

start_time = timeit.default_timer()
#print(depth_first_search(root,8))
depth_first_search(root,8)
elapsed = timeit.default_timer() - start_time
print("Recursive depth:")
print(elapsed)