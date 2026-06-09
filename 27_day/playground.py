def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,2,3,4,5))


def calculate(n,**kwargs):
    print(kwargs)

    n += kwargs["add"]
    n -= kwargs["subtract"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    print(n)

calculate(n=2,add=3, multiply=5, subtract = 9, divide= 2)



# *args and **kwargs
# *args many arguments
# **kwargs many arguments with keywords, access like dict