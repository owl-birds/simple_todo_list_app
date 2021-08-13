# SHow the user his/her todo list
def show_list(todo_list: list):
    if len(todo_list) == 0:
        print("-------------------------")
        print("     TODO LIST EMPTY     ")
        print("-------------------------")
    else:
        print("-------------------------")
        print("          TODOs          ")
        print("-------------------------")
        idx = 0
        for todo in todo_list:
            idx += 1
            print(str(idx)+"."+todo[:len(todo)-1])
        print("-------------------------")


def show_menu():
    print("------------------------------")
    print("             MENU             ")
    print("------------------------------")
    print("Choose one (1-5)")
    print("------------------------------")
    print("1. Show the list")
    print("2. Adding a new todo")
    print("3. Remove a todo")
    print("4. Remove/Clear all Todos")
    print("5. EXIT (saved)")
    print("------------------------------")
