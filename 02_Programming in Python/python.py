import os

# aprendendo meus primeiros skills em python


def say_hello():
    print("Hello")


def variables():
    a, b = 3, 4
    print(a)
    print(b)

def name():
    name = "Otavio"
    a = name[0]
    print(a)

def concatenation():
    a = "minha comida favorita é "
    b = "pizza"
    c = a + b
    print(c)

def say_hello(you):
    return "Hello " +  you

def working_with_numbers():
    user_num_1 = input("First number is: ")
    user_num_2 = input("Second number is: ")
    user_sum = user_num_1 + user_num_2
    print(user_sum)

if __name__ == '__main__':
    #say_hello()
    #variables()
    #name()
    #concatenation()
    #print(say_hello("Otavio"))
    working_with_numbers()