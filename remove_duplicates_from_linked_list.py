from __future__ import annotations

class Node:
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head

    def remove_duplicates(self) -> None:
        node = self.head
        hash = { node.data }
        while node and node.next:
            if node.next.data in hash:
                node.next = node.next.next
            else:
                hash.add(node.next.data)
            node = node.next
    
    def print(self) -> None:
        node = self.head
        while node:
            print(f'{node.data}', end='')
            if node.next:
                print(', ', end='')
            node = node.next

def main():
    linkedList = LinkedList(Node(1, Node(2, Node(7, Node(2, Node(27, Node(7)))))))
    linkedList.remove_duplicates()
    linkedList.print()

if __name__ == '__main__':
    main()