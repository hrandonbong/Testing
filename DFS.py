class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    # TODO: Write your code here
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here
    path_helper(root, sum, allPaths, [])
    return allPaths


def path_helper(current, currentSum, paths, arr):
    """
    :param current:        the current node in the BST
    :param currentSum:         The current sum we are looking for
    :param paths:    An array of all the paths we have found
    :param arr:         The temporary array
    :return:            Returns nothing
    """
    if current is None:
        return

    arr.append(current.val)

    if currentSum == current.val and current.left is None and current.right is None:
        # list function is needed so that a copy of the current array is saved
        paths.append(list(arr))

    path_helper(current.left, currentSum - current.val, paths, arr)
    path_helper(current.right, currentSum - current.val, paths, arr)
    del arr[-1]


def find_sum_of_path_numbers(root):
    return sum_helper(root, 0)


def sum_helper(root, total):
    if root is None:
        # I need to return a zero because currently integers are being added
        # at the end of this function
        return 0

    total = total * 10 + root.val

    if root.left is None and root.right is None:
        return total

    return sum_helper(root.left, total) + sum_helper(root.right, total)


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
