# Main program for Linked List Implementation
import sys
from Code.LinkedList.SinglyLinkedList import LinkedList as Lst


def user_input():
    print("Please Enter the Value to be inserted as data of the Node")
    return input()


def user_get_index():
    print("Please Enter the location where the Node will be Inserted/Deleted ")
    return input()


def print_info():
    print("Please use the below commands for Linked list creation")
    print("1 - Create a node in the List")
    print("2 - Create node at the start of the List")
    print("3 - Create node at the middle of the List")
    print("4 - Create node at the end of the List")
    print("5 - Delete node from the start of the List")
    print("6 - Delete node from the middle of the List")
    print("7 - Delete node from the end of the List")
    print("0 - Display the list")
    print("-1 - Print Final list and Exit the Program")


if __name__ == '__main__':
    print("Welcome to Linked List")
    print_info()
    lst = Lst.LinkedList()
    while True:
        print("Enter your choice")
        choice = input()
        while choice != "-1":
            if choice == "1":
                data = user_input()
                lst.add_node(data)
                break
            elif choice == "2":
                data = user_input()
                lst.add_node_at_starting(data)
                break
            elif choice == "3":
                data = user_input()
                location = int(user_get_index())
                lst.add_node_in_between(data, location)
                break
            elif choice == "4":
                data = user_input()
                lst.add_node_at_end(data)
                break
            elif choice == "5":
                lst.delete_start_node()
                break
            elif choice == "6":
                location = int(user_get_index())
                lst.delete_node_at_position(location)
                break
            elif choice == "7":
                lst.delete_end_node()
                break
            elif choice == "0":
                print("Displaying the List")
                lst.display()
                break
            else:
                print("WRONG CHOICE...")
                print_info()
                print("************* Please Enter The number in the above range ****************")
                break
        if choice == "-1":
            print(str.format("The number of nodes in the list are : {0}", lst.length()))
            print("***** Below is the Complete Linked List *****")
            lst.display()
            print("Press 0 to Exit")
            do_exit = input()
            if do_exit == "0":
                sys.exit("Thank you Exiting Program")
