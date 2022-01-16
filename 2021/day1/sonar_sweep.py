input_file = open('input.txt', 'r')
depths = list(map(int, input_file.read().splitlines()))

increment = 0

for i in range(len(depths) - 1):
    if depths[i] < depths[i + 1]:
        increment += 1
        
print(f"Number of increment: {increment}")
input_file.close()