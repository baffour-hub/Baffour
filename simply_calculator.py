def add (numbers):
    return sum(numbers)

def subtract (numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply (numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
    
def divide (numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result
