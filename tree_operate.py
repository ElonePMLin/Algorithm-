import collections


class LockingTree:

    def __init__(self, parent):
        self.locked = {}
        self.children = collections.defaultdict(list)
        for i, p in enumerate(parent):
            # parent[i]  i's parent
            self.children[parent[i]].append(i)
        self.parent = parent
        self.flag = False

    def lock(self, num: int, user: int) -> bool:
        # user_one lock
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        # user_one unlock
        if num in self.locked and user == self.locked[num]:
            del self.locked[num]
            return True
        return False

    def sub_unlock(self, sub):
        for i in sub:
            if self.unlock(i, self.locked.get(i, None)):
                self.flag = True
            self.sub_unlock(self.children[i])

    def upgrade(self, num: int, user: int) -> bool:
        # parent none lock
        # sub-children loack(lock by anybody)
        # cur-node none lock
        # finally, unlock sub-children

        tmp = num
        while self.parent[tmp] != -1:
            if self.parent[tmp] in self.locked:
                return False  # 祖父节点 已经上锁
            tmp = self.parent[tmp]

        self.sub_unlock(self.children[num])
        if not self.flag:
            return False
        self.flag = False

        # upgrade
        if not self.lock(num, user):
            return False  # 当前节点 已经锁上
        return True


op = ["upgrade","upgrade","upgrade","upgrade","upgrade","lock","unlock","upgrade","upgrade","upgrade",
      "lock","upgrade","upgrade","upgrade","lock","unlock","upgrade","unlock","unlock","upgrade"]
args = [[9,43],[4,27],[5,34],[7,31],[4,27],[2,47],[7,21],[4,12],[1,1],[8,20],[5,50],[5,28],[0,11],[6,19],[9,27],[5,6],[0,5],[4,49],[4,22],[5,27]]
obj = LockingTree([-1,4,9,0,6,1,0,6,3,1])
ret = [False] * len(op)
for i, (num, user) in enumerate(args):
    if op[i] == "upgrade":
        ret[i] = obj.upgrade(num, user)
    elif op[i] == "lock":
        ret[i] = obj.lock(num, user)
    elif op[i] == "unlock":
        ret[i] = obj.unlock(num, user)

print(ret,   [False, False, False, False, False, True, False, True, False, False, True, False, False, True, True, False, False, False, False, False])
print(ret == [False, False, False, False, False, True, False, True, False, False, True, False, True, False, True, False, False, False, False, False])
# [false,false,false,false,false,true,false,true,false,false,true,false,true,false,true,false,false,false,false,false]
