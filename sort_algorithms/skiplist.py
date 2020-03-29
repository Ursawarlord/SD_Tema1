import random

class Node(object):
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList(object):
    def __init__(self, max_lvl, P):
        self.MAXLVL = max_lvl
        self.P = P      # P e fractia nodurilor cu nivelul i
        self.header = self.createNode(self.MAXLVL, -1)
        self.level = 0

    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n

    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and \
                lvl < self.MAXLVL: lvl += 1
        return lvl

    def insert_all(self, list_keys):
        for x in list_keys:
            self.insertElement(x)

    def insertElement(self, key):
        update = [None] * (self.MAXLVL + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and \
                    current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current == None or current.key != key:
            rlevel = self.randomLevel()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel
            n = self.createNode(rlevel, key)
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

    def return_sorted_List(self):
        sorted = []
        head = self.header
        for lvl in range(self.level + 1):
            # print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while (node != None):
                # print(node.key, end=" ")
                sorted.append(node.key)
                node = node.forward[lvl]
            # print("")
        return sorted