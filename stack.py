class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements (top → bottom):")
            while current:
                print(current.data)
                current = current.next

    # 🟢 NEW METHODS REQUIRED BY YOUR INSTRUCTIONS
    def remove_beginning(self):
        """Removes the first (top) element."""
        if self.top is None:
            return None
        removed = self.top.data
        self.top = self.top.next
        return removed

    def remove_at_end(self):
        """Removes the last element in the stack (bottom)."""
        if self.top is None:
            return None
        if self.top.next is None:
            removed = self.top.data
            self.top = None
            return removed

        current = self.top
        while current.next.next:
            current = current.next

        removed = current.next.data
        current.next = None
        return removed

    def remove_at(self, data):
        """Removes the first node with the given data."""
        if self.top is None:
            return None

        # If the top node is the one to remove
        if self.top.data == data:
            removed = self.top.data
            self.top = self.top.next
            return removed

        current = self.top
        while current.next:
            if current.next.data == data:
                removed = current.next.data
                current.next = current.next.next
                return removed
            current = current.next

        return None  # Not found

    def display(self):
        if self.top is None:
            return "Empty"
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result)
