import src.calculator as calculator

selection = int(input(
    "\nSelect your calculator option: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n"))

num1 = int(input("\nProvide your first value:\n"))
num2 = int(input("\nProvide your second value:\n"))

if selection == 1:
    output = calculator.add(num1, num2)

# code goes here
if selection == 2:
    output = calculator.subtract(num1, num2)

if selection == 3:
    output = calculator.multiply(num1, num2)

if selection == 4:
    output = calculator.divide(num1, num2)

print("\nOutput: " + str(output))
