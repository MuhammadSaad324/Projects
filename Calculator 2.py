logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# Addition
def add (n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1-n2

# Multiplication
def multiply(n1,n2):
    return n1*n2

# Division
def division(n1,n2):
    return n1/n2

all_operators={"+":add,"-":subtract,"*":multiply,"/":division}

number1=int(input("What's Your First Number? "))
for operators in all_operators:
    print(operators)
pick_operators=input("Pick An Operator ")
number_2=int(input("What's Your Second Number? "))
result=all_operators[pick_operators](number1,number_2)
print(f"{number1} {pick_operators} {number_2} = ",result)

next_calculation=True
while next_calculation:
    new_calculation=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation? ").lower()
    if new_calculation =="y":
        number1=result

        for operators in all_operators:
            print(operators)
        pick_operators = input("Pick An Operator ")

        number_2 = int(input("What's Your Second Number? "))
        result = all_operators[pick_operators](number1, number_2)
        print(f"{number1} {pick_operators} {number_2} = ", result)

    elif new_calculation=="n":
        number1 = int(input("What's Your First Number? "))
        for operators in all_operators:
            print(operators)
        pick_operators = input("Pick An Operator ")
        number_2 = int(input("What's Your Second Number? "))
        result = all_operators[pick_operators](number1, number_2)
        print(f"{number1} {pick_operators} {number_2} = ", result)