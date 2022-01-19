with open('input.txt') as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = [int(i) for i in numbers.split(',')]
    all_boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]
    
def is_marked(board):
    # check row is marked fully
    for row in range(len(board)):
        if sum(board[row]) == -5:
            return True
        
    # checks if column is marked fully
    total = 0
    for row in range(len(board)):
        for col in range(len(board)):
            total += board[col][row]
        if total == -5:
            return True
    return False
            
# summation of all unmarked numbers
def calc_unmarked_numbers(board):
    total = 0
    for row in board:
        for val in row:
            if val != -1:
                total += val
                
    return total

def solve():
    for number in numbers:
        for board in all_boards:
            total = 0
            for row in range(len(board)):
                for col in range(len(board)):
                    if number == board[row][col]:
                        temp = board[row][col]
                        board[row][col] = -1
                        total += 1
                        if is_marked(board):
                            total_value = calc_unmarked_numbers(board)
                            return total_value * temp
                                
print(solve())
    