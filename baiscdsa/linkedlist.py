# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# a = Node(10)
# b = Node(12)
# c = Node(13)
# print(a.data)
# print(b.data)
# print(c.data)

# print(id(a))
# print(id(b))
# print(id(c))

# a.next = b
# b.next = c

# print(a.next)
# print(b.next)
# print(c.next)
# print(int(0x1051AC550))
# print(int(0x1051AC690))


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Empty linked list => Head = None that is empty linked list because empty linked list does not contain any value inside head in the begining
        self.head = None
        self.n = 0  # that represent how many node in my linked list

    # length of the linked list is number of the node inside linked list
    def __len__(self):
        return self.n
        # here n representing lenth of node (number of node inside linked list)

    # Linked List containe 4 methods mainly
    # 1. Insert
    # 2. Traverse
    # 3. Delete
    # 4. Search

    # Insert have three methods to insert data in any linked list
    # 1. Insert from head
    # 2. Insert from tail (append called in list)
    # 3. Insert from middle (insert called in list)
    def insert_head(self, value):
        # create new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increament of n so we can track how many nodes in my linked list
        self.n = self.n + 1

    # insert from tail (we will create append method bcz in list insert from last we called append)
    def append(self, value):
        # create new node using Node Class
        new_node = Node(value)

        # code for if linked list already empty
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return

        # create current variale for storing head
        curr = self.head
        while curr.next != None:  # we stopped loop here just before last node
            curr = curr.next
        # loop stopped now you are at the last node
        curr.next = new_node
        # increament n for track how many node in our linked list
        self.n = self.n + 1

    # insert middle
    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        # here are two cases
        # 1. break -> element found -> curr not None
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return "Item not found"

    # Traverse in linked list
    # 1. print
    # def traverse(self):
    #     curr = self.head
    #     while curr != None:
    #         print(curr.data)
    #         curr = curr.next

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            # print(curr.data)
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]  # removing last arrow from result


# Delete in linked list
# 1. Head
# 2. Teal (pop called in list)
# 3. Value (remove called in list )
# 4. Index

# Search
# 1. Value
# 2. Index

L = LinkedList()
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(3)
# L.insert_head(4)
# L.append(3)
# L.append(13)
# L.append(88)
print(L.insert_after(2, 25))
print(L)
# print(len(L))
