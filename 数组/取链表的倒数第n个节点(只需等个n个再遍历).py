# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        node = head
        ans = head
        while node:
            node = node.next
            if cnt > 0:
                cnt -= 1
            else:
                ans = ans.next
        return ans


    