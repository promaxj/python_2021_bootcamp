

def add(n1, n2):
    return n1 +  n2
def subtract(n1, n2):
    return n1  - n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

v = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

first_num = int(input("please input a first number?"))
for dic in dictionary:
    print(dic)
operration_symbol = input("please pick an operration form the line above.")
calculation_function = operration_dictionary[operration_symbol]
second_num = int(input("please input a second number?"))

answer = operration_dictionary

print(f"{first_num} {operration_symbol} {second_num} = {answer}")