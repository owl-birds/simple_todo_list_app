from modules.Database import Database
import modules.app_funcs as app_funcs


# DATABASE TESTING
# db_test = Database()
# print(db_test.data)
# db_test.add_data("sleeping")
# print(db_test.data)
# db_test.remove_data(3)
# print(db_test.data)
# db_test.save_data()
# print(db_test.data[2][0:len(db_test.data[2])-1])
# print(type(db_test))


# TESTING SHOW TODO LIST FUNC
# modules.app_funcs.show_list([])
# modules.app_funcs.show_list(db_test.data)

# print(db_test.data)
# db_test.remove_all_data()
# print(db_test.data)


# BUILDING THE  APPS

# LOADING TODO list from txt file
db_todo = Database()

# app_funcs.show_list(db_todo.data)


# APPS logic
while True:
    app_funcs.show_menu()
    try:
        user_input = int(input("Enter your choice : "))
    except:
        print("INPUT ERROR")
    # EXIT
    if user_input == 5:
        db_todo.save_data()
        print("EXITING THE APP, AND SAVING THE TODO")
        break
    # SHOW THE LIST
    elif user_input == 1:
        try:
            app_funcs.show_list(db_todo.data)
        except:
            print("SHOW LIST FUNC ERROR!!! in option 1")
        try:
            user_input = int(input("press enter to continue"))
        except:
            print("option 1, show list ERROR")
    # ADDING A TODO
    elif user_input == 2:
        new_todo = input("Enter new todo : ")
        try:
            db_todo.add_data(new_todo)
        except:
            print("ADDING NEW TODO ERROR")
    # REMOVE A TODO
    elif user_input == 3:
        try:
            app_funcs.show_list(db_todo.data)
        except:
            print("SHOW LIST FUNC ERROR!!! in option 3")

        try:
            user_input = int(input("ENTER THE TODO's index: (0 to cancel)"))
        except:
            print("remove a todo input error")
        # CANCEL REMOVAL
        if user_input == 0:
            print("cancelled")
            user_input = input("press enter to continue")
            continue
        try:
            db_todo.remove_data(user_input-1)
            print("todo removed")
        except:
            print("remove a todo ERROR!!!, please put the right index number")
        user_input = input("press enter to continue")
    # REMOVE ALL TODO /CLEAR
    elif user_input == 4:
        try:
            db_todo.remove_all_data()
        except:
            print("REMOVE ALL TODO ERROR!!!")
        print("ALL TODOS REMOVED")
        user_input = input("press enter to continue")
        pass
