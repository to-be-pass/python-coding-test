def solution(decimal : int) -> str:
    """ convert decimal number to binary
    
    Args:
      decimal(int) : decimal integer
    Returns:
      converted binary number(str)
    """
    stack = []
    while decimal > 0:
        stack.append(str(decimal % 2))
        decimal >>= 1
    
    stack.reverse()
    return "".join(stack)

def solution2(decimal : int) -> str:
    """ another solution with built-in method
    
    Args:
      decimal(int) : decimal integer
    Returns:
      converted binary number(str)
    """
    return "{0:#b}".format(decimal)

if __name__ == "__main__":
    import timeit

    arguments = [
        ['1', '0', '0', '0', '0', '1'],
        ['1', '1', '0', '1', '1', '1', '0', '0'],
        ['0', '1', '0', '0', '1', '0', '0', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1',
          '1', '0', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '0', '1']

    ]

    methods = [
        "ret = ''\nwhile stack:\n\tret += stack.pop()",
        "ret = ''.join(reversed(stack))",
        "stack = reversed(stack); ret = ''.join(stack)",
        "ret = ''.join(stack[::-1])",
        "stack = stack[::-1]; ret = ''.join(stack)",
        "ret = ''.join(list(reversed(stack)))",
        "stack.reverse(); ret = ''.join(stack)"
    ]

    for arg in arguments:
        print(f"parameter : {arg}")
        for method in methods:
            stmt = f"stack = {arg}; {method}"
            print(f"{method} method executed in {timeit.timeit(stmt, number=10_000_000)} elapsed time")