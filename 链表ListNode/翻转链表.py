# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        pre = None
        while node:
            nxt = node.next  # 保存下一个节点
            node.next = pre  # 翻转箭头
            pre = node  # 指向当前位置
            node = nxt  # 更新下一个节点

        return pre
