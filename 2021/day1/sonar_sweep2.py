input_file = open('input.txt', 'r')
depths = list(map(int, input_file.read().splitlines()))

# [0, 1, 2] - [1, 2, 3]
# no need to check 1st and 2nd indexes since they exist in both summation
# hence, check i, i + 3 for every iteration
def solve():
    increase = 0
    for i in range(0, len(depths)- 3):
        if depths[i + 3] > depths[i]:
            increase += 1
    
    print(increase)
    
solve()