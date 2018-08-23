class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution():

    def copyList(self, head):
        hash_map = {}
        if head == None:
            return None
        head1 = RandomListNode(head.label)
        hash_map[head] = head1
        Acopy = head1
        if head.random != None:
            if head.random not in hash_map:
                temp = RandomListNode(head.random.label)
                hash_map[head.random] = temp
            else:
                temp = hash_map[head.random]
            head1.random = temp
        while head.next != None:
            if head.next not in hash_map:
                temp = RandomListNode(head.next.label)
                hash_map[head.next] = temp
            else:
                temp = hash_map[head.next]
            Acopy.next = temp
            Acopy = Acopy.next
            head = head.next
            if head.random != None:
                if head.random not in hash_map:
                    temp = RandomListNode(head.random.label)
                    hash_map[head.random] = temp
                else:
                    temp = hash_map[head.random]
                Acopy.random = temp
        return head1
