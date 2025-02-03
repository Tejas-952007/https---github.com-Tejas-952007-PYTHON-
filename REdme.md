# Simple Python Calculator

This is a simple Python calculator program that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The program allows the user to select an operation, input two numbers, and get the result. The user can continue performing multiple calculations until they choose to exit the program.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second (with validation to prevent division by zero).

## Requirements

- Python 3.x or higher.

## How to Run the Program

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/simple-python-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd simple-python-calculator
    ```

3. Run the Python script:
    ```bash
    python calculator.py
    ```

4. Follow the prompts to select an operation and enter two numbers.

## Example Usage

### Program Flow:

1. **Choose an operation**:
   ```bash
   Select operation.
   1.Add
   2.Subtract
   3.Multiply
   4.Divide
Enter numbers:
Enter first number: 5
Enter second number: 3

Result:
5.0 + 3.0 = 8.0

Continue or Exit:
Let's do next calculation? (yes/no): no
Exiting the program. Goodbye!

Example Output:
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 1
Enter first number: 5
Enter second number: 3
5.0 + 3.0 = 8.0
Let's do next calculation? (yes/no): yes

Enter choice(1/2/3/4): 4
Enter first number: 10
Enter second number: 2
10.0 / 2.0 = 5.0
Let's do next calculation? (yes/no): no
Exiting the program. Goodbye!
