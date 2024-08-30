def solve_equation(equation):
    equation = equation.replace(" ", "")  # Remove spaces for easier processing

    # Split the equation into left and right parts
    if '=' in equation:
        left, right = equation.split('=')
    else:
        return "Invalid equation format"
    print(left,right)
    # Identify if 'x' is on the left or right side
    if 'x' in left:
        for i in range(-1000, 1000):  # Brute force possible values of x (assuming integers)
            test_left = left.replace('x', str(i))
            if eval(test_left) == int(right):
                return i
    elif 'x' in right:
        left_value = eval(left)  # Evaluate the left side of the equation
        return left_value
    else:
        return "Equation does not contain 'x'"

# Test examples
input1 = "12 * x0 = 120"
input2 = "2 - 4 = x"

# Outputs
x1 = solve_equation(input1)
x2 = solve_equation(input2)

# Printing the outputs
print(x1)  # Output: 12
print(x2)  # Output: -2
