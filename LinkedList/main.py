from linked_list import *


if __name__ == '__main__':

    # Create a new LinkedList
    ll = LinkedList()

    # Add new items
    ll.add_item(1)
    ll.add_item(30)
    ll.add_item(101)
    ll.add_item(-9)
    ll.add_item(22)

    # List all items in a LinkedList
    ll.list_items()

    # Remove items from a LinkedList
    ll.remove_item()
    print("=== Items after One Remove Operations ====")
    ll.list_items()

    # Find 2nd item in a LinkedList
    print("==========================================")
    print("2nd item in the LinkedList is ::{}".format(ll.find(2)))
