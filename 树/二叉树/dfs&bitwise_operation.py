# dfs
class FindElements:
    def __init__(self, root):
        self.valSet = set()
        self.dfs(root, 0)  # 传入的是root对象，无论怎么操作都是对root对象进行操作

    def find(self, target: int) -> bool:
        return target in self.valSet

    def dfs(self, node, val: int):
        if node is None:
            return
        node.val = val
        self.valSet.add(val)
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)


class FindElements:
    def __init__(self, root):
        self.dfs(root, 0)
        self.root = root

    def dfs(self, node, val: int):
        if node is None:
            return
        node.val = val
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)

    # 位运算（需要进一步推理关系才能想到这个方法，即要熟记这个关系，leetcode 1261）
    def find(self, target: int) -> bool:
        target += 1  # +1换算后，使位运算0为左，1为右
        k = target.bit_length() - 2  # 由于0+1后1为初始位，不参与位运算，因此需要-2（1，10，11。如k=2，k-2，即从第0位开始计算）
        node = self.root
        while k >= 0 and node is not None:  # for 和 while 写法不同，都能实现提前结束循环
            if (target & (1 << k)) == 0:  # 左移、右移写法不同，但结果一样
                node = node.left
            else:
                node = node.right
            k -= 1
        return node is not None

# bfs
# target = 4
# print(target.bit_length())  # 提取字节长度

