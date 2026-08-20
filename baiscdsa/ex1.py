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

    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def __delitem__(self, key):
        if 0 <= key < self.n:
            for i in range(key, self.n - 1):
                self.A[i] = self.A[i + 1]

            self.n = self.n - 1

    def __getitem__(self, key):

        if key < 0:
            key = self.n + key

        if 0 <= key < self.n:
            return self.A[key]
        else:
            return "IndexError - Index out of range"

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n = self.n + 1

    def sort(self):
        for i in range(self.n - 1):
            for j in range(self.n - 1 - i):
                if self.A[j] > self.A[j + 1]:
                    self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]

    def min(self):
        if self.n == 0:
            return "Empty List"

        minimum = self.A[0]

        for i in range(1, self.n):
            if self.A[i] < minimum:
                minimum = self.A[i]
        return minimum

    def max(self):
        if self.n == 0:
            return "Empty List"

        max = self.A[0]

        for i in range(1, self.n):
            if self.A[i] > max:
                max = self.A[i]
        return max

    def sum(self):
        if self.n == 0:
            return "Empty List"

        total = 0
        for i in range(self.n):
            total += self.A[i]

        return total

    def extend(self, items):
        for item in items:
            self.append(item)

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
# l.append("Hello")
# l.append(True)
# l.append(100)
# l.append(900)
# l.append(800)
# l.pop()
# l.clear()
# print(len(l))
# print(l.find("Hellojj"))
# l.insert(0, 0)
# del l[3000]
# print(l.remove(1000))

l.append(6)
l.append(5)
l.append(3)
l.append(9)
l.append(7)
l.append(2)
# print(l)
# l.sort()
# print(l)
# print(l.sort())
# print(l.min())
# print(l.max())
# print(l.sum())
# l.extend([10, 11, 12])
print(l[-1])
print(l)
