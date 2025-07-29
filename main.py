HISTORY_FILE = "history.txt" # File PATH

def showHistory():
    with open(HISTORY_FILE, "r") as f:
        length = len(f.readlines())
        if length == 0:
            print("History is empty.")
        else:
            with open(HISTORY_FILE, "r") as f:
                print(f.read())
            
def clearHistory():
    with open(HISTORY_FILE, "w") as f:
        f.write("")
        
    print("History has been cleared.")
        
def saveHistory(expression , result):
    with open(HISTORY_FILE, "r+") as f:
        f.write(expression + " = " + str(result) + "\n")
            
    print("History has been saved.")
        
def add(a , b):
    return a + b
    
def subtract(a , b):
    return a - b
    
def multiply(a , b):
    return a * b
def divide(a , b):
    return a / b
def power(a , b):
    return a ** b
def mod(a , b):
    return a % b
def floor(a , b):
    return a // b

    

while True:
    
    # print()
    
    expression = input("Enter Expresion with Operator ( + , - , * , / , ^ , % , //) or (exit , history , clear): ")
    
    if expression == "exit":
        print("Calculator has been closed.")
        break
    elif expression == "history":
        showHistory()
    elif expression == "clear":
        clearHistory()
    else:
        try:
            result = eval(expression)
            print(result)
            saveHistory(expression , result)
        except:
            print("Invalid Expression")
            


