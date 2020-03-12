from Task_2 import *

lst = {}
def create_instance():
    names()
    try:
        with open("names.txt") as file:
            for row in file:
                row = row.strip("\n")
                instance = NewUsers((row.rsplit(' ', 1)[0]))
                lst[instance] = row
    except FileNotFoundError:
        print("That file does not exist!")
        return
    finally:
        print("The instances have been created")


def read_info():
    for item in lst:
        item.name_len()


create_instance()
read_info()
