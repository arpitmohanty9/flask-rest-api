def multiply(*args):
    # print(args)
    # print(type(args))
    total = 1
    for arg in args:
        total = total * arg
    
    return total


print(multiply(1,3,5))

print(multiply(1,3,5,6,7,9,0))
print(multiply(1,))
print(multiply())

# * is used to collect arguments into one parameters


# Destructuring the arguments into multiple paramers
print("Destructuring python arguments")

def add(x,y):
    return x + y

nums = [3,5]
print(add(*nums))

print(add(x=3,y=5))

nums = {"x":15, "y":25}

print(add(nums["x"], nums["y"])) # lot of square brackets not easy to read 
print(add(x=nums["x"], y=nums["y"])) # lot of square brackets not easy to read 


print(add(**nums)) #destructuring args



def apply(*args, operator):
    # keyword arguements
    pass


## named arguments into dictionary
def named(**kwargs):
    print(kwargs)


named(name="Arpit", age="33")


### unpac a dictionary into named variables using **
def named2(name,age):
    print(name,age)

details = {"name": "Arpit", "age": "31"}

named(**details)