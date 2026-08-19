import ctypes


class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # we have to create ctype array with size = self.size
        self.A = self._make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        return "[" + result[:-1] + "]"

    def pop(self):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):

        for i in range(self.n):
            if self.A[i] == item:
                return i

        return "ValueError - item not in list"

    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        self.A[pos] = item
        self.n = self.n + 1

    def __delitem__(self, key):
        for i in range(key, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.n = self.n - 1

    def __getitem__(self, key):
        if 0 <= key < self.n:
            return self.A[key]
        else:
            return "IndexError - Index out of range"

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self._make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassining A
        self.A = B

    def _make_array(self, capacity):
        return (
            capacity * ctypes.py_object
        )()  # this code create a ctypes array with size capacity


l = MyList()
# print(type(l))
# print(l)
l.append("Hello")
l.append(True)
l.append(100)
l.append(900)
l.append(800)
# l.pop()
# l.clear()
# print(len(l))
# print(l.find("Hellojj"))
# l.insert(0, 0)
del l[3]
print(l)
