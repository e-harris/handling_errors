# # Taks 1
# I want a program to ask for food.
# As a user I should be able to ask for any amount of food.#
# As I user I should be able to create different orders (different files)
# As a user I should be able to read back the order to my client
# **Acceptance criterea**
# - it should be well formated
# - it should be numbered
# example
# ```python
# > 1 - Nachos
# > 2 - Diet CocaCola
# ```
# As a user, if I try to read a order that doens't exist it should give me an error.
# As a user I should be able to amend my order :)
# ## DOD
# - is its own project
# - git and github
# - simple documentation
# - functional
# - separation of concerns
# - it should handle errors

def food():
    count = 1
    customer_name = input("What is your name? \n"
                          "> ")
    ask1 = input("What would you like to order? \n"
                 "> ")
    order = [ask1]
    while True:
        ask2 = input("Anything else? \n"
                     "> ")
        count += 1
        if ask2.lower() != "no":
            order.append(ask2)
        if ask2.lower() == "no":
            break
    try:
        customer_order = open(f"{customer_name}.txt", "a")
        num = 0
        for item in order:
            num += 1
            customer_order.write(str(num) + ") " + item.title() + '\n')
            print(f"{num}) {item.title()}")
        customer_order.close()
    except FileNotFoundError as error:
        print("Error, file does not exist!")
        print(error)
    finally:
        print("End of program")

food()
