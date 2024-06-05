import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    numbers = re.sub(r'\n', ',', numbers)
    num_list = list(map(int, numbers.split(",")))
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(num_list)
