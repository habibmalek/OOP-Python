class linked_list():
    def __init__(self, data):
        self.head = Node(data, None)

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def ispalindrome(self):
        leftpointer = self.head
        list = []
        ispal = True

        # addine linkedlist nodes to list
        while leftpointer is not None:
            list.append(leftpointer.data)
            leftpointer = leftpointer.next
        
        # comparing list elements using pop with linkedlist nodes value 
        # from frist node with the last one as we poping it from list
        while self.head is not None:
            i = list.pop()
            if self.head.data == i:
                ispal = True
            else:
                ispal = False
                break
            self.head = self.head.next
        return print(ispal)


    def insert(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode


    def printlist(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# Manual Creation & Insertion of Linkedlist

list1 = linked_list(1)
node1 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
list1.head = node1
node1.next = node3
node3.next = node4
node4.next = node5

list1.insert(6)
print("######################")
list1.reverse()
list1.printlist()

print("######################")
list2 = linked_list(7)
list2.insert(1)
list2.insert(2)
list2.insert(7)
list2.insert(9)
list2.insert(8)
list2.printlist()

print("######################")
r = linked_list(1)
r.insert(2)
r.insert(2)
r.insert(2)
r.insert(1)

list2.ispalindrome()
r.ispalindrome()

print("######################")

# find the intersection between 2 linkedlist after defining another linkedlist 

list1.printlist()
print("######################")
list2.printlist()
print("######################")

g = list1.head
l1 = []
while g is not None:
    l1.append(g.data)
    g = g.next
print("This is the elements of list 1 >>>",l1)


d = list2.head
l2 = []
while d is not None:
    l2.append(d.data)
    d = d.next
print("This is the elements of list 2 >>>",l2)

l3 = list(set(l1) & set(l2))
print("This is the intersection element between the two lists >>>",l3)

