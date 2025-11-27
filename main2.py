
def funct(first: int, sign: str, second: int):
    if sign == "+":
        result = first + second
    elif sign == "-":
        result = first - second
    elif sign == "*":
        result = first * second
    elif sign == "/":
        result = first / second
    return f"{first} {sign} {second} = {result}"

print(funct(12,"+", 13))

