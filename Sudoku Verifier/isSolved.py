def isSolved(puzzle) :
    solved = False
    
    finished = checkFinished(puzzle)
    if (finished) :
        solved = checkSolution(puzzle)
    
    return solved
    
def checkFinished(puzzle) :
    finished = True
    if (len(puzzle) == 9) :
        for sub in puzzle :
            if (len(sub) == 9) :
                for integer in sub :
                    if (integer > 9) or (integer < 1) :
                        finished = finished and False
            else :
                finished = finished and False
    else :
        finished = finished and False
    
    return finished
    
def checkSolution(puzzle) :
    # first check the rows
    check = checkRows(puzzle)
    print("Rows pass? " + str(check))
    
    # then, if needed, check the columns,
    if (check) :
        columns = getColumns(puzzle)
        check = check and checkArrays(columns)
        print("Columns pass? " + str(check))
    
        # then, if needed, check the boxes
        if (check) :
            boxes = check and getBoxes(puzzle)
            check = check and checkArrays(boxes)
            print("Boxes pass? " + str(check))
    
    return check
    
def checkRows(puzzle) :
    if not isinstance(puzzle, list) :
        return False
    if not isinstance(puzzle[0], list) :
        return False
        
    okay = True
    for sub in puzzle :
        okay = okay and checkGroup(sub)
        # print(sub)
        # print("Pass: " + str(checkGroup(sub)))
        # print()
        
    return okay
    
def getColumns(puzzle) :
    if not isinstance(puzzle, list) :
        return None
    if not isinstance(puzzle[0], list) :
        return None
    
    columns = []
    for i in range(len(puzzle)) :
        # use the ith index of each sub-puzzle
        column = []
        for sub in puzzle :
            column.append(sub[i])
        columns.append(column)
    return columns
    
def checkArrays(arrays) :
    okay = True
    for puzzle in arrays :
        okay = okay and checkGroup(puzzle)
        # print(puzzle)
        # print("Pass: " + str(checkGroup(puzzle)))
        # print()
        
    return okay

# partition into 9 3x3 boxes represented by 1D arrays    
def getBoxes(puzzle) :
    if not isinstance(puzzle, list) :
        return None
    if len(puzzle) is not 9 :
        return None
    
    for sub in puzzle :
        if not isinstance(sub, list) :
            return None
        if len(sub) is not 9 :
            return None
    
    boxes = []
    
    for i in range (0,3) :
        rowSection = puzzle[(i*3):((i+1)*3)] # get 3 rows per section
        for j in range (0,3) : # j indicates the column
            roughBox = [] # rough because it'll be an array containing 3 arrays
            
            # for each row in the secion 
            for k in range(0,3) :
                roughBox.append(rowSection[k][(j*3):(j+1)*3])
            
            # retrieve the contents of the inner arrays
            box = []
            for sub in roughBox :
                for item in sub :
                    box.append(item)
            
            boxes.append(box)
    
    return boxes
    
# givem 9 numbers, check to see if 1..9 are all in there
def checkGroup(group) :
    if not isinstance(group, list) :
        return False
    if (len(group) is not 9) :
        return False
        
    okay = True
    numbers = [1,2,3,4,5,6,7,8,9]
    
    for i in range(len(numbers)) :
        # check if each number is in group
        for member in group :
            if (numbers[i] == member) :
                numbers[i] = 0
    
    for number in numbers :
        if number > 0 :
            okay = okay and False
    
    return okay