
# 1) Local scope

def get_total(a,b):
    # local variable declared inside a function
    total = a + b
    return total

print(get_total(5,2))
# print(total) # NameError: name 'total' is not defined



# 2) Enclosing scope

def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()

get_total(5,5)


# 3) Global scope

special = 5

def get_total(a,b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #Local variable
        double = total * 2
        print(special)
    
    double_it()
    return total

print(get_total(10,5))