# returns content
def read_file():
    f = open('input.txt', 'r')
    binary_numbers = f.read().split('\n')
    return binary_numbers
    
    
def convert_binary_to_decimal(binary):
    val, power = 0, 0
    print(f'binary: {binary}')
    for i in range(len(binary), 0, -1):
        print(f'val: {val}, uslu: {2 ** power} binary_last: {binary[i - 1]}')
        val += ((2 ** power) * int(binary[i - 1])) 
        power += 1
    print(f'last val: {val}')
    return val
    
def solve():
    # take it as 2d array
    content = read_file()
    r, c = 0, 0
    gamma, epsilon = '', ''
    for r in range(len(content[0])):
        zeros, ones = 0, 0
        for c in range(len(content)):
            if content[c][r] == '0':
                zeros += 1
            else: 
                ones += 1
        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
            
    print(f'gamma: {gamma}, epsilon: {epsilon}')
    first = convert_binary_to_decimal(gamma)
    second = convert_binary_to_decimal(epsilon)
    
    print(f'{first} * {second} = {first*second}')
            
solve()