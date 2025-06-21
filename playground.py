# *args in python Function
def add (*args):
    x = 0
    for n in args:
        x += n
    return x
print(add(23,45,66,89,21,39,22,45,90))

# kwargs in python Function
def foo (a,**kwargs):
    n = 0
    n += kwargs ["num_1"]
    n*= kwargs ["num_2"]
    return n * a
print(foo(12,num_1 = 5, num_2 = 4))

# Problem 1

def sum_all(*args):
    n = 0
    for number in args:
        n += number
    return n
print(sum_all(1,2,3,4,5,6,7,8,9))

# Problem 2
def find_max(*args):
    return max(args)

print(find_max(12, 34, 56, 78, 90))

# Problem 3
def custom_join(separator, *args):
    if not args:
        return ""

    args = [str(arg) for arg in args]

    result = args[0]
    for i in range(1, len(args)):
        result += separator + args[i]

    return result

print(f"Example 1: {custom_join('-', 'a', 'b', 'c')}")

# Problem 4 Count Even Numbers
def count_even(*args):
    all_even = []
    for even in args:
        if even % 2 == 0:
            all_even.append(even)
    return (len(all_even))
print(count_even(12,34,56,444,21,31,33))

# Problem 5
def multiply_all(*args):
    y  = 1
    for numbers in args:
        y *= numbers
    return y
print(multiply_all(1,2,4,5,6,7,8,9))

# Problem 6
def print_user_info(**kwargs):
    print(f"Name: {kwargs["Name"]}, Age: {kwargs["Age"]}")
print_user_info(Name = "John", Age = 30)


# Problem 7
def calculate_price(**kwargs):
    total = kwargs["apple"] + kwargs ["banana"] + kwargs["pineapple"]
    return total
print(calculate_price(apple=30, banana=15,pineapple=130))

# Problem 8
