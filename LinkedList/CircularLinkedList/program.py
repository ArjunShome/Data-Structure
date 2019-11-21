import sys
from Code.LinkedList.CircularLinkedList.LinkedList import CircularLinkedList


def user_input():
    print("Please Enter the Value to be inserted as data of the Node")
    return input()


def user_get_index():
    print("Please Enter the location where the Node will be Inserted/Deleted ")
    return input()


def print_info():
    print("Please use the below commands for Linked list creation")
    print("1 - Insert to the List")
    print("2 - Insert at particular location in the list")
    print("3 - Append to the List")
    print("4 - Delete element at a particular location from the List")
    print("5 - Delete particular data from the List")
    print("6 - Delete from end of the List")
    print("7 - Display the list")
    print("-1 - Print Final list and Exit the Program")


if __name__ == '__main__':
    print("Welcome to Circular Linked List")
    print_info()
    lst = CircularLinkedList()
    while True:
        print("Enter your choice")
        choice = input()
        while choice != "-1":
            if choice == "1":
                data = user_input()
                lst.insert(data)
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
                lst.remove(position=location)
                break
            elif choice == "5":
                print('Enter the value to be deleted')
                data = input()
                lst.remove(data=data)
                break
            elif choice == "6":
                lst.remove()
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
            print("***** Below is the Complete Circular Linked List *****")
            lst.display()
            print("Press 0 to Exit")
            do_exit = input()
            if do_exit == "0":
                sys.exit("Thank you Exiting Program")
