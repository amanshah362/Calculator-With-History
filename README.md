# Calculator with History

A simple command-line calculator in Python that supports basic arithmetic operations and maintains a history of calculations in a text file.

## Features

- Supports addition, subtraction, multiplication, division, power, modulus, and floor division.
- Saves each calculation to a history file.
- View or clear calculation history.
- Exit command to close the calculator.

## Usage

1. Run the calculator:
    ```sh
    python main.py
    ```

2. Enter expressions using operators: `+`, `-`, `*`, `/`, `^`, `%`, `//`
    - Example: `5 + 4 * 2`

3. Special commands:
    - `history` — Show calculation history.
    - `clear` — Clear calculation history.
    - `exit` — Exit the calculator.

## Files

- [`main.py`](main.py): Main calculator script.
- [`history.txt`](history.txt): Stores calculation history.

## Example

```
Enter Expresion with Operator ( + , - , * , / , ^ , % , //) or (exit , history , clear): 5 + 4
9
History has been saved.
Enter Expresion...: history
5 + 4 = 9
```

---
