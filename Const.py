from functools import singledispatchmethod
from Byte import Byte


class Const:
    @singledispatchmethod
    def __init__(self, x):
        self.x = [Byte(x)] + [Byte(0)] * 15

    @__init__.register(str)
    def _from_str(self, x):
        pairs = [Byte(int(x[i:i+2], 16)) for i in range(0, 31, 2)]
        self.x = pairs

    @__init__.register(list)
    def _from_list(self, x):
        self.x = x

    def __ilshift__(self, other):
        self.x = self.x[1:]
        return self

    def __irshift__(self, other):
        self.x = self.x[:-1]
        return self

    def __str__(self):
        return f'{"".join([str(l) for l in self.x])}'

    def __repr__(self):
        return f'{"".join([str(l) for l in self.x])}'

    def __iadd__(self, other):
        self.x = self.x + [other]
        return self

    def __isub__(self, other):
        self.x = [other] + self.x
        return self

    def __getitem__(self, item: int):
        return self.x[item]
