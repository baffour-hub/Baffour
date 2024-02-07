from simply_calculator import*

while True:
    arithmetic_expression = input("Enter arithmetic expression (example: '2 * 4 - 5 / 6') or '!' to exit calculator: ")
    
    if arithmetic_expression == '!' :
        print("Calculator Exited")
        break
    try:
        result = eval(arithmetic_expression)
        print(f"Result of the arithmetic expression: {arithmetic_expression} = {result}")
    except Exception as e:
        print(f"Error: {e}")
   