import art


def add(n1, n2):
    return n1 + n2

# TODO write out the other 3 functions subtract, multiply, divide
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# my_favourite_number = divide
# print(my_favourite_number(2,4))
# TODO add these 4 functions into a dictionary as the values. key= "+","-","*","/"
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}



# we can use another while loop and also use def fucntion to solve
# should_calculator = True
# while should_calculator:
def calculator():
    print(art.logo)
    should_accumulate = True
    number1 =float(input("Enter The First Number: "))


    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input(" pick the operation : " )
        number2 = float(input("Enter The Next Number: "))
        answer = operation[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"type 'y' for continue calculating with {answer}, or type 'N' for new Calculation: ").lower()
        if choice == 'y':
            number1 = answer
        else:
            should_accumulate = False
            # if we can use while loop than this line is required
            # should_calculator = True
            print("\n" * 3)
            calculator()

calculator()