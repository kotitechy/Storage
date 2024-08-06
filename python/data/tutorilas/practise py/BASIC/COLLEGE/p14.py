class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(2))          # Output: 2
print(calc.add(2, 3))       # Output: 5
print(calc.add(2, 3, 4))    # Output: 9
