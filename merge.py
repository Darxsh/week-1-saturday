class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

def create_linked_list(arr):
    ll = LinkedList()
    for num in arr:
        ll.append(num)
    return ll

# Input arrays
arr1 = [3, 8, 4, 12]
arr2 = [15, 1, 6, 19]

# Sort the input arrays to create sorted linked lists
arr1.sort()
arr2.sort()

# Create linked lists
ll1 = create_linked_list(arr1)
ll2 = create_linked_list(arr2)

# Merge the sorted linked lists
merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)

# Convert the merged linked list back to a list and print the result
merged_list = LinkedList()
merged_list.head = merged_head
print(merged_list.to_list())
