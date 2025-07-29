HISTORY_FILE = "history.txt" # FILE PATH

def showHistory():
    with open(HISTORY_FILE, "r") as f:
        length = len(f.readlines())
        if length == 0:
            print("History is empty.")
        else:
            f.seek(0)
            print(f.read())

def clearHistory():
    with open(HISTORY_FILE, "w") as f:
        f.write("")
    print("History has been cleared.")

def saveHistory(expression, result):
    with open(HISTORY_FILE, "a") as f:  # Use 'a' to append instead of 'r+'
        f.write(expression + " = " + str(result) + "\n")
    print("History has been saved.")

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def power(a, b): return a ** b
def mod(a, b): return a % b
def floor(a, b): return a // b

def all_operation():
    return add, subtract, multiply, divide, power, mod, floor


print("\n" + "\t" * 9 + "Calculator With History")

while True:
    print()
    expression = input("Enter expression ( + , - , * , / , ^ , % , // ) or (exit , history , clear): ")

    if expression.lower() == "exit":
        print("Calculator has been closed.")
        break
    elif expression.lower() == "history":
        showHistory()
    elif expression.lower() == "clear":
        clearHistory()
    else:
        try:
            expression = expression.replace("^", "**")  # Handle power operator
            result = eval(expression)
            print("Result:", result)
            saveHistory(expression, result)
        except Exception as e:
            print("Invalid Expression:", e)
