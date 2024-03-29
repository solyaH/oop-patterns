import math
from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, data, result):
        self.data = data
        self.result = result

    @abstractmethod
    def get_answer(self):
        return

    @abstractmethod
    def get_score(self):
        return

    @abstractmethod
    def get_loss(self):
        return


class A(Base):
    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y)
                    in zip(ans, self.result)]) / len(ans)

    def get_loss(self):
        return sum([(x - y) * (x - y) for (x, y) in zip(self.data,
                                                        self.result)])


class B(A):
    def get_loss(self):
        return -sum([y * math.log(x) + (1 - y) * math.log(1 - x)
                     for (x, y) in zip(self.data, self.result)])

    def get_pre(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans,
                                                        self.result)]
        return sum(res) / sum(ans)

    def get_rec(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans,
                                                        self.result)]
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(A):
    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data,
                                                 self.result)])


if __name__ == '__main__':
    list1 = [0.8, 0.2, 0.1]
    list2 = [1, 1, 1]
    a = A(list1, list2)
    b = B(list1, list2)
    c = C(list1, list2)
    print(a.get_answer())
    print(b.get_answer())
    print(c.get_answer())

    print(a.get_loss())
    print(b.get_loss())
    print(c.get_loss())

    print(a.get_score())
    print(b.get_score())
    print(c.get_score())
