# Task 2 with oop
# The object is to practice everything up to this point.
#
# objectives:
#
# create a text file with 10 names
#
# create a class for NewUsers()
#
# it should only require 1 argument to be created, a name?
# have another python file that will:
#
# read the txt file
# create 10 object from said file
# have a method in you NewUser that:
#
# outputs a text file with information about the user
# Don't forget: - definition of done - handling errors

def names():
    try:
        with open("names.txt", 'w') as names_file:
            print("Please provide 10 names:")
            for number in range(1, 11):
                name = input("> ")
                names_file.write(f"{number} - {name} \n")
    except FileNotFoundError:
        print("That file does not exist!")
        return


class NewUsers:
    def __init__(self, name):
        self.name = name

    def details(self, name):
        return name

    def name_len(self):
        print(len(self.name))


