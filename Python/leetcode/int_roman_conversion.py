def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    for i in range(len(values)):
        value = values[i]
        symbol = symbols[i]
        while num >= value:
            result += symbol
            num -= value
    
    return result
num=int(input())
print(int_to_roman(num))
