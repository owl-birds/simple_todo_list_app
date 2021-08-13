from typing import Text


class Database():
    def __init__(self, path: str = "C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES\OOP\\mini_project\\todo_list_app\\the_apps\\database\\data.txt") -> None:
        # showing the path to database
        self.path = path
        # Change the path to txt file based on where your txt
        # file saved

        # TAKING DATA from txt file
        txt_open = open(self.path, "r")
        data = txt_open.readlines()
        txt_open.close()
        # DATA
        self.data = data

    def add_data(self, todo: str):
        self.data.append(todo+"\n")

    def save_data(self):
        txt_open = open(self.path, "w+")
        for dt in self.data:
            txt_open.write(dt)
        txt_open.close()

    def remove_all_data(self):
        self.data.clear()
        txt_open = open(self.path, "w+")
        txt_open.write("")
        txt_open.close()

    def remove_data(self, idx: int):
        self.data.pop(idx)

    # or maybe just run the function in the __init__ function
    # yeah lets do that

    # alternative func
    # def take_data_txt(self):
    #     # reading data from txt file and saving it into
    #     # llist type variable called data and returning it
    #     # back as a list
    #     txt_open = open(self.path, "r")
    #     data = txt_open.readlines()
    #     txt_open.close()  # closing the file
    #     # return it or maybe save it into the class

    #     # opt 1
    #     # return data
    #     # opt2
    #     self.data = data
