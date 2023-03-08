def initialize_world(file_name):
    try:
        file = open(file_name, "r")
        world = [[single for single in line.strip()] for line in file]
    except FileNotFoundError:
        world = []
        single_line = "-" * 20
        for index in range(8):
            world.append(list(single_line))
        print("The File is NOT Found. An Empty World is Used in the Program.")
    return world


def count_neighbors(world, row, col):
    neighbors_num = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if i < 0 or j < 0 or i >= len(world) or j >= len(world[0]):
                continue
            if world[i][j] == '*':
                neighbors_num += 1
    return neighbors_num


def compute_next_generation(world):
    new_world = []
    for i in range(len(world)):
        new_row = []
        for j in range(len(world[i])):
            num_neighbors = count_neighbors(world, i, j)
            if world[i][j] == '*' and (num_neighbors == 2 or num_neighbors == 3):
                new_row.append('*')
            elif world[i][j] == '-' and num_neighbors == 3:
                new_row.append('*')
            else:
                new_row.append('-')
        new_world.append(new_row)
    return new_world


def display_world(world, generation):
    print("The Generation " + generation + " : ")
    for row in world:
        print(''.join(row))


def main():
    file_name = "Life.txt"
    world = initialize_world(file_name)
    display_world(world, "0")
    for generation in range(1, 11):
        world = compute_next_generation(world)
        display_world(world, str(generation))


if __name__ == '__main__':
    main()
