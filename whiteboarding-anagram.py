class Node:
    def __init__(self):
        self.data = data
        self.next = None

    def __repr__(self):
    return "<Node object. Data: {}; Next: {}>".format(
                                    self.data,
                                    self.next.data if self.next else None,
                                    )
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "<Linked List. Head: {}; Tail: {}>".format(
                                        self.head.data if self.head else None,
                                        self.tail.data if self.head else None,
                                        )

    def grouping(lst):
        