class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def find_minimum_depth(root):
    # TODO: Write your code here
    queue = []
    depth = 1
    queue.append(root)
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)

            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth


def find_successor(root, key):
    # TODO: Write your code here
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        if node.val == key:
            break

    return queue[0] if queue else None


class TreeNodeLink:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    # TODO: Write your code here
    queue = []
    queue.append(root)
    prev = None

    while queue:
        node = queue.pop(0)
        if prev:
            prev.next = node
        prev = node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return

def tree_right_view(root):
    result = []
    queue = []
    queue.append(root)

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            if i == size - 1:
                result.append(node)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    # TODO: Write your code here
    return result

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))