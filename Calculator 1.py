# Simple Calculator
number_1=int(input("What's Your First Number? "))
operators=["+","-","*","/","**"]
for operator in operators:
    print(operator)
pick_operator = input("Pick An Operation? ")
number_2=int(input("What's the next number? "))

# Use If Else Logic
def calculator(num1,op,num2):
    if type(num1) !=int:
        return
    if type(num2) != int:
        return
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op =="/":
        return num1 / num2
    elif op == "**":
        return num1 ** num2
final_value=calculator(number_1,pick_operator,number_2)
print(f"{number_1} {pick_operator} {number_2} =",final_value)

next_calculation=True

while next_calculation:
    new_calculation=input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start new calculation? ").lower()
    if new_calculation == "y":
        number_1=final_value
        operators = ["+", "-", "*", "/", "**"]
        for operator in operators:
            print(operator)
        pick_operator = input("Pick An Operation? ")
        number_2 = int(input("What's the next number? "))
        final_value=calculator(number_1,pick_operator,number_2)
        print(f"{number_1} {pick_operator} {number_2} = ",final_value)
    elif new_calculation == 'n':
        number_1 = int(input("What's Your First Number? "))
        operators = ["+", "-", "*", "/", "**"]
        for operator in operators:
            print(operator)
        pick_operator = input("Pick An Operation? ")
        number_2 = int(input("What's the next number? "))
        final_value = calculator(number_1, pick_operator, number_2)
        print(f"{number_1} {pick_operator} {number_2}" ,final_value)