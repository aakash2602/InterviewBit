
class Node:

    def __init__(self, num):
        self.num  = num
        self.next = None

class Linked_List:

    def __init__(self):
        self.head = None

    def insert_node(self, node):
        new_node = node
        start = self.head

        if start == None:
            self.head = new_node
            return

        if start.num > new_node.num:
            new_node.next = start
            self.head = new_node
            return

        while start.next != None:
            if start.next.num > new_node.num:
                new_node.next = start.next
                start.next = new_node
                break
            start = start.next

        if start.next == None:
            start.next = new_node

        return

    def delete_node(self, num):
        start = self.head

        if start.num == num:
            self.head = start.next
            return

        mode = 0
        while start.next != None:
            if start.next.num == num:
                start.next = start.next.next
                mode = 1
                break
            start = start.next

        if mode == 0:
            print ("Node not present in Linked List")

        return

    def pprint(self):
        start = self.head
        print (start.num, end="")
        while start.next != None:
            print ('-->' + str(start.next.num), end='')
            start = start.next
        print ()


if __name__ == "__main__":
    llist = Linked_List()
    new_node = Node(5)
    llist.insert_node(new_node)
    new_node = Node(10)
    llist.insert_node(new_node)
    new_node = Node(7)
    llist.insert_node(new_node)
    new_node = Node(3)
    llist.insert_node(new_node)
    new_node = Node(1)
    llist.insert_node(new_node)
    new_node = Node(9)
    llist.insert_node(new_node)

    llist.pprint()

    llist.delete_node(5)
    llist.pprint()

    llist.delete_node(1)
    llist.pprint()