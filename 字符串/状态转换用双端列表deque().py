from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        # 双端列表
        q = deque()
        flag = True
        for c in s:
            if c == 'i':
                flag = not flag
                continue
            if flag:
                q.append(c)
            else:
                q.appendleft(c)
        return ''.join(q if flag else reversed(q))
