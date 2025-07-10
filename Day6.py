def load_data():
    data = []
    with open("input/day6.txt", "r") as file:
        for line in file.readlines():
            data.append(list(line.strip()))  
    file.close()                      
    return data

def solve(data=None):
    ## Part one:
    ## Rule: if something in front turn right 90 degrees 
    ## Rule: else step forward
    # mark stepped on spots with X to count at the end
    # reaching a bound  terminates loop
    if data is None:
        data = load_data()

    sum_X = 0
    # find position of guard
    guard_pos = []
    for r in range(len(data)):
        for c in range(len(data[r])):
        #multi type lists are a sin
            if data[r][c] == "^":
                guard_pos = [r,c, 0]
            if data[r][c] == ">":
                guard_pos = [r, c, 90]
            if data[r][c] == "<":
                guard_pos = [r,c, 270]
            if data[r][c] == "v":
                guard_pos = [r,c, 180]
            
    
    
    # simulate guards route 
    while((guard_pos[0] > 0 and guard_pos[1] >0) and guard_pos[0] < len(data) -1 and guard_pos[0] < len(data[0]) -1 ):
        r = guard_pos[0]
        c = guard_pos[1]
        if guard_pos[2] == 0:
            if data[r-1][c] == "#":
                data[r][c] = ">"
                guard_pos = [r,c, 90]
            else: 
                data[r][c] = "X"
                data[r-1][c] = "^"
                guard_pos = [r-1, c, 0]
        elif guard_pos[2] == 90:
            if data[r][c+1] == "#":
                data[r][c] = "v"
                guard_pos = [r,c, 180] 
            else: 
                data[r][c] = "X"
                data[r][c+1] = ">"
                guard_pos = [r,c+1, 90]
        elif guard_pos[2] == 180:
            if data[r+1][c] == "#":
                data[r][c] = "<"
                guard_pos = [r,c, 270] 
            else: 
                data[r][c] = "X"
                data[r+1][c] = "v"
                guard_pos = [r+1,c, 180]

        elif guard_pos[2] == 270:
            if data[r][c-1] == "#":
                data[r][c] = "^"
                guard_pos = [r,c, 0] 
            else: 
                data[r][c] = "X"
                data[r][c-1] = "<"
                guard_pos = [r,c-1, 270]

    data[guard_pos[0]][guard_pos[1]] = "X" # mark the final position

    for r in data:
        sum_X+= r.count("X")

    # if loop:
    #     return sum x    

    return sum_X


##part 2 
# place an additional object in each potential position and see which ones would cause a looop. 
# defined by if guard returns to start with same initial direction. 
# def solve2():
#     loops = 0
#     data = load_data()
#     for r in range(len(data)):
#         for c in range(len(data[r])):
#             if data[r][c] != "#":
#                 data_temp = data
#                 data_temp[r,c] == "#"
#                 sumX, loops += solve(data)

        



def main():
    print(solve())
    # print(solve2)

if __name__ == "__main__":
    main()