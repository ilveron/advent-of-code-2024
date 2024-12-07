import os
from itertools import product

def has_correct_combination(test_value, equation, operators):
    n = len(equation)-1     # number of needed operators
    combinations_of_operators = product(operators, repeat=n)
    for combination in combinations_of_operators:
        result = equation[0]
        for idx in range(len(combination)):
            next_number = equation[idx+1]
            op = combination[idx]
            if op == '+':
                result += next_number
            elif op == '*':
                result *= next_number
            elif op == '||':
                result = int(str(result)+str(next_number))
            else:
                raise Exception("Cannot do operation with operator:", op)
            
        if result == test_value:
            return True
    return False


def main():
    test_values_and_equation = {}
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            split_on_colon = line.strip().split(':')
            test_value, equation = (int(split_on_colon[0]), [int(value) for value in split_on_colon[1].split(" ")[1:]])      # slice from idx 1 on since the first char after the colon is a whitespace 
            test_values_and_equation[test_value] = equation     

        part1_result = part2_result = 0

        for test_value, equation in test_values_and_equation.items():
            if has_correct_combination(test_value, equation, ('+','*')):
                part1_result += test_value
                part2_result += test_value
            elif has_correct_combination(test_value, equation, ('+','*','||')):
                part2_result += test_value
        
        print(f"part1: {part1_result}")
        print(f"part2: {part2_result}")

if __name__ == '__main__':
    main()