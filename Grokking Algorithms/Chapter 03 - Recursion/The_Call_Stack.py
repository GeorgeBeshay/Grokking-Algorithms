def greet_2(name):
    print("How Are You, " + name + "??")


def bye():
    print("Ok Bye !!")


def greet(name):
    print("Hello, " + name + "!")
    greet_2(name)
    print("Getiing Ready to Say Bye ...")
    bye()


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


greet("George")
print(fact(5))
