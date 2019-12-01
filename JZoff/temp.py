
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listnode(strnum):
    h = ListNode(strnum[0])
    p = h
    for i in range(1, len(strnum)):
        num = strnum[i]
        p.next = ListNode(num)
        p = p.next
    return h


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = TreeNode(-1)

    def isEmpty(self):
        return True if self.root.val == -1 else False

    def add(self, data):
        node = TreeNode(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.left == None:
                    tree_node.left = node
                    return
                elif tree_node.right == None:
                    tree_node.right = node
                    return
                else:
                    queue.append(tree_node.left)
                    queue.append(tree_node.right)

    def pre_order(self, start):
        node = start
        if node == None:
            return
        print(node.val)
        if node.left == None and node.right == None:
            return
        self.pre_order(node.left)
        self.pre_order(node.right)

    def pre_order_loop(self):
        if self.isEmpty():
            return
        stack = []
        node = self.root
        while node or stack:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                node = node.right

    def in_order(self, start):
        node = start
        if node == None:
            return
        self.in_order(node.left)
        print(node.val)
        self.in_order(node.right)

    def in_order_loop(self):
        if self.isEmpty():
            return
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                print(node.val)
                node = node.right
