# Python
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self, arr):
        self.head = None
        self.tail = None
        self.size = 0
        self.keys = set()
        for key in arr:
            self.addlast(key)

    def addlast(self, key):
        if key not in self.keys:
            node = Node(key)
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node
            self.size += 1
            self.keys.add(key)

    def addfirst(self, key):
        if key not in self.keys:
            node = Node(key)
            node.next = self.head
            self.head = node
            if self.tail is None:
                self.tail = node
            self.size += 1
            self.keys.add(key)

    def addafter(self, u, v):
        if u not in self.keys and v in self.keys:
            curr = self.head
            while curr and curr.key != v:
                curr = curr.next
            node = Node(u)
            node.next = curr.next
            curr.next = node
            if curr == self.tail:
                self.tail = node
            self.size += 1
            self.keys.add(u)

    def addbefore(self, u, v):
        if u not in self.keys and v in self.keys:
            prev = None
            curr = self.head
            while curr and curr.key != v:
                prev = curr
                curr = curr.next
            node = Node(u)
            node.next = curr
            if prev is None:
                self.head = node
            else:
                prev.next = node
            self.size += 1
            self.keys.add(u)

    def remove(self, key):
        if key in self.keys:
            prev = None
            curr = self.head
            while curr and curr.key != key:
                prev = curr
                curr = curr.next
            if prev is None:
                self.head = curr.next
            else:
                prev.next = curr.next
            if curr == self.tail:
                self.tail = prev
            self.size -= 1
            self.keys.remove(key)

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head, self.tail = self.tail, self.head

    def print(self):
        curr = self.head
        while curr:
            print(curr.key, end=" ")
            curr = curr.next
        print()


n = int(input())
arr = list(map(int, input().split()))
ll = LinkedList(arr)
command = input()
while command != "#":
    args = command.split()
    if args[0] == "addlast":
        ll.addlast(int(args[1]))
    elif args[0] == "addfirst":
        ll.addfirst(int(args[1]))
    elif args[0] == "addafter":
        ll.addafter(int(args[1]), int(args[2]))
    elif args[0] == "addbefore":
        ll.addbefore(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        ll.remove(int(args[1]))
    elif args[0] == "reverse":
        ll.reverse()
    command = input()
ll.print()
