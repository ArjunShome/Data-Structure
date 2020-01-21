# Main program for Linked List Implementation
import sys
from Code.LinkedList.DoubleeLinkedList import LinkedList as Lst


def user_input():
    print("Please Enter the Value to be inserted as data of the Node")
    return input()


def search_user_input():
    print("Please Enter Value to be Searched")
    return input()


def user_get_index():
    print("Please Enter the location where the Node will be Inserted/Deleted ")
    return input()


def print_info():
    print("Please use the below commands for Linked list creation")
    print("1 - Prepend to the List")
    print("2 - Insert to the List")
    print("3 - Append to the List")
    print("4 - Delete from the List")
    print("5 - Pop the list")
    print("6 - Search in the list")
    print("7 - Display the list")
    print("-1 - Print Final list and Exit the Program")


if __name__ == '__main__':
    print("Welcome to Linked List")
    print_info()
    lst = Lst.DoubleeLinkedList()
    while True:
        print("Enter your choice")
        choice = input()
        while choice != "-1":
            if choice == "1":
                data = user_input()
                lst.prepend(data)
                break
            elif choice == "2":
                data = user_input()
                location = int(user_get_index())
                lst.insert(data, location)
                break
            elif choice == "3":
                data = user_input()
                lst.append(data)
                break
            elif choice == "4":
                location = int(user_get_index())
                lst.delete(location)
                break
            elif choice == "5":
                lst.pop()
                break
            elif choice == "6":
                print("Starting Search.....")
                data = search_user_input()
                lst.search(data)
                break
            elif choice == "7":
                print("Displaying the List")
                lst.display()
                break
            else:
                print("WRONG CHOICE...")
                print_info()
                print("************* Please Enter The number in the above range ****************")
                break
        if choice == "-1":
            print(str.format("The number of nodes in the list are : {0}", len(lst)))
            print("***** Below is the Complete Linked List *****")
            lst.display()
            print("Press 0 to Exit")
            do_exit = input()
            if do_exit == "0":
                sys.exit("Thank you Exiting Program")
