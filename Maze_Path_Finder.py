def print_maze(MP):
    for i in range(0, 3):
        for j in range(0, 3):
            print(MP[i][j], end=" ")
        print()


def initialize_maze():
    M = [['1', '2', '3'], ['4', 'X', '5'], ['6', '7', 'E']]
    Original_Maze = [[0, 0, 0], [0, -1, 0], [0, 0, 2]]
    print_maze(M)
    select = input("Select the Starting position (S) in the Maze from 1-7: ")
    if select == "1":
        M[0][0] = 'S'
        Original_Maze[0][0] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "2":
        M[0][1] = 'S'
        Original_Maze[0][1] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "3":
        M[0][2] = 'S'
        Original_Maze[0][2] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "4":
        M[1][0] = 'S'
        Original_Maze[1][0] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "5":
        M[1][2] = 'S'
        Original_Maze[1][2] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "6":
        M[2][0] = 'S'
        Original_Maze[2][0] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    elif select == "7":
        M[2][1] = 'S'
        Original_Maze[2][1] = 1
        print("Maze will be:")
        print_maze(M)
        return Original_Maze
    else:
        print("Select from the given positions")
        Original_Maze = initialize_maze()
        return Original_Maze


Maze = initialize_maze()
start_found = False
start_found_row = -1
start_found_col = -1
end_found = False
pathArray = []
for r in range(0, 3):
    for c in range(0, 3):
        if Maze[r][c] == 1:
            start_found = True
            start_found_row = r
            start_found_col = c
        if start_found:
            if start_found_row == 0:
                if r == 0:
                    pathArray.append([r, c])
        if start_found:
            if start_found_row == 0:
                if r == 1:
                    pathArray.append([1, 2])
                    break
        if start_found:
            if start_found_row == 0:
                if r == 2:
                    pathArray.append([2, 2])
                    break
        if start_found:
            if start_found_row == 1:
                if r == 1:
                    pathArray.append([r, c])
                    break
        if start_found:
            if start_found_row == 1:
                if r == 2:
                    if start_found_col == 2:
                        pathArray.append([r, start_found_col])
                        break
                    elif start_found_col == 0:
                        pathArray.append([r, c])
        if start_found:
            if start_found_row == 2:
                pathArray.append([r, c])

print("Path coordinates from start (S) to end (E) are:", pathArray)