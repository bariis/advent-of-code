# returns content
def read_file():
    f = open('input.txt', 'r')
    binary_numbers = f.read().split('\n')
    return binary_numbers

def convert_binary_to_decimal(binary):
    val, power = 0, 0
    print(f'binary: {binary}')
    for i in range(len(binary), 0, -1):
        print(f'val: {val}, power: {2 ** power} binary_last: {binary[i - 1]}')
        val += ((2 ** power) * int(binary[i - 1])) 
        power += 1
    print(f'last val: {val}')
    return val

def remove_zeros(binary_numbers, bit_position):
    print(f'bit_position: {bit_position}, inside 1')
    i = 0
    while i < len(binary_numbers):
        if binary_numbers[i][bit_position] == '0':
            before = len(binary_numbers)
            removed_number = binary_numbers[i]
            binary_numbers.remove(binary_numbers[i])
            print(f'i: {i} before: {before}, after: {len(binary_numbers)}, removed number: {removed_number}')
            i -= 1
        i += 1    
    
    return binary_numbers

def remove_ones(binary_numbers, bit_position):
    print(f'bit_position: {bit_position}, inside 0')
    i = 0
    while i < len(binary_numbers):
        if binary_numbers[i][bit_position] == '1':
            before = len(binary_numbers)
            removed_number = binary_numbers[i]
            binary_numbers.remove(binary_numbers[i])
            print(f'i: {i} before: {before}, after: {len(binary_numbers)}, removed number: {removed_number}')
            i -= 1
        i += 1
    
    return binary_numbers
    

def find_rating_in_binary(binary_numbers, type):
    one_counter, zero_counter = 0, 0
    bit_position = 0
    while len(binary_numbers) != 1:
        one_counter, zero_counter = 0, 0
        print(f'length: {len(binary_numbers)}, numbers: {binary_numbers}')
        r = 0
        for binary in binary_numbers:
            if binary[bit_position] == '0':
                zero_counter += 1
            else:
                one_counter += 1
        if type == 'oxygen':
            if one_counter >= zero_counter:
                binary_numbers = remove_zeros(binary_numbers, bit_position)
            else:
                binary_numbers = remove_ones(binary_numbers, bit_position)
        else:
            if zero_counter <= one_counter:
                binary_numbers = remove_ones(binary_numbers, bit_position)
            else:
                binary_numbers = remove_zeros(binary_numbers, bit_position)
                    
        bit_position += 1
    return binary_numbers[0]
                    
def solve():
    binary_numbers = read_file()
    second_list = list(binary_numbers)
    
    oxy_binary = find_rating_in_binary(binary_numbers, 'oxygen')
    co2_binary = find_rating_in_binary(second_list, 'co2')
    print(f'co2_binary: {co2_binary}')
    print(f'oxy_binary: {oxy_binary}')
    
    oxy = convert_binary_to_decimal(oxy_binary)
    co2 = convert_binary_to_decimal(co2_binary)
    print(f'oxygen generator rating: {oxy}')
    print(f'co2 scrubber rating: {co2}')
    print(f'{oxy} * {co2} = {oxy * co2}')
            
solve()