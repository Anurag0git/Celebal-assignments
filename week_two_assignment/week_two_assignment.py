class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListError(Exception):
    pass


class LinkedList:
  
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
    
    def delete_nth_node(self, n):
        if not self.head:
            raise LinkedListError("Cannot delete from an empty list.")
        if n < 1 or n > self.size:
            raise LinkedListError(f"Index {n} is out of range. List has {self.size} elements.")
        if n == 1:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        for i in range(1, n - 1):
            current = current.next

        node_to_delete = current.next
        current.next = node_to_delete.next
        self.size -= 1
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.head is None


def test_linked_list():
   
    print("=== Testing Singly Linked List Implementation ===\n")
    ll = LinkedList()
    
    print("1. Test empty list:")
    ll.print_list()
    print(f"Size: {ll.get_size()}")
    print(f"Is empty: {ll.is_empty()}\n")
    
    print("2. Adding elements to the list:")
    elements = [10, 20, 30, 40, 50]
    for element in elements:
        ll.add(element)
        print(f"Added {element}")
    
    print("\nCurrent list:")
    ll.print_list()
    print(f"Size: {ll.get_size()}")
    print(f"Is empty: {ll.is_empty()}\n")
    
    print("3. Test valid deletions:")
    
    try:
        print("Deleting 3rd node (value 30):")
        ll.delete_nth_node(3)
        ll.print_list()
        print(f"Size after deletion: {ll.get_size()}\n")
    except LinkedListError as e:
        print(f"Error: {e}\n")
    
    try:
        print("Deleting 1st node (value 10):")
        ll.delete_nth_node(1)
        ll.print_list()
        print(f"Size after deletion: {ll.get_size()}\n")
    except LinkedListError as e:
        print(f"Error: {e}\n")
    
    print("4. Testing exception handling:")
    
    while not ll.is_empty():
        ll.delete_nth_node(1)
    
    print("List after deleting all nodes:")
    ll.print_list()
    
    try:
        print("Trying to delete from empty list:")
        ll.delete_nth_node(1)
    except LinkedListError as e:
        print(f"Caught exception: {e}\n")
    
    print("5. Testing invalid index handling:")
    
    ll.add(100)
    ll.add(200)
    ll.add(300)
    
    print("Current list:")
    ll.print_list()
    
    invalid_indices = [0, -1, 5, 10]
    for index in invalid_indices:
        try:
            print(f"Trying to delete node at index {index}:")
            ll.delete_nth_node(index)
        except LinkedListError as e:
            print(f"Caught exception: {e}")
    
    print(f"\nFinal list:")
    ll.print_list()
    print(f"Final size: {ll.get_size()}")


if __name__ == "__main__":
    test_linked_list()
