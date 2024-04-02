#Define a function called remove_node(), The function should remove the ith node of the linked list (index from 0) and return the modified head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, items=None):
        self.head = None
        if items:
            for item in items:
                self.append(item)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def flatten(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next_node
        return result


def remove_node(head, i):
  if i < 0:
    return head
  if head is None:
    return None
  if i == 0:
    return head.next_node
  head.next_node = remove_node(head.next_node, i- 1)
  return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())

###LinkedList not defined properly