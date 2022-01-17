def solve():
    horizontal, depth, aim = 0, 0, 0
    input_file = open('input.txt', 'r')
    content = input_file.read()
    content_list = content.split("\n")
    for instruction in content_list:
        inst = instruction.split(' ')
        move = int(inst[1])
        print(f'inst: {inst[0]}, move: {move}')
        if inst[0] == 'up':
            aim -= move
        elif inst[0] == 'down':
            aim += move
        else:
            horizontal += move
            depth += aim * move
    
    print(f'horizontal: {horizontal}, depth: {depth}')
    return horizontal * depth
    
print(solve())