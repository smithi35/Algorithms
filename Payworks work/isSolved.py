def isSolved(array) :
    solved = False
    
    finished = checkFinished(array)
    if (finished) :
        solved = checkSolution(array)
    
    return solved
    
def checkFinished(array) :
    finished = True
    if (len(array) == 9) :
        for sub in array :
            s = ""
            if (len(sub) == 9) :
                for integer in sub :
                    if (integer > 9) or (integer < 1) :
                        finished = finished and False
                        print("There was a number greater than 9 or less than 1, which is not allowed")
            else :
                finished = finished and False
                
    else :
        finished = finished and False
        
    print("Finished = " + str(finished))
    
    return finished
    
def checkSolution(array) :
    # first check the rows
    check = checkRows(array)
    print("Rows pass? " + str(check))
    
    # then, if needed, check the columns,
    if (check) :
        columns = getColumns(array)
        check = check and checkArrays(columns)
        print("Columns pass? " + str(check))
    
        # then, if needed, check the boxes
        if (check) :
            boxes = check and getBoxes(array)
            check = check and checkArrays(boxes)
    
    return check
    
def checkRows(array) :
    okay = True
    for sub in array :
        okay = okay and checkGroup(sub)
        print(sub)
        print("Pass: " + str(checkGroup(sub)))
        print()
        
    return okay
    
def getColumns(array) :
    columns = []
    for i in range(0, 9) :
        # use the ith index of each sub-array
        column = []
        for sub in array :
            column.append(sub[i])
        columns.append(column)
    return columns
    
def checkArrays(arrays) :
    okay = True
    for array in arrays :
        okay = okay and checkGroup(array)
        print(array)
        print("Pass: " + str(checkGroup(array)))
        print()
        
    return okay

# partition into 9 3x3 boxes represented by 1D arrays    
def getBoxes(array) :
    boxes = []
    
    for i in range (0,3) :
        rowSection = array[(i*3):((i+1)*3)]
        for j in range (0,3) :
            roughBox = []
            
            # for each row in the secion
            for k in range(0,3) :
                roughBox.append(rowSection[k][(j*3):(j+1)*3])
            
            # then just remove the inside arrays
            box = []
            for sub in roughBox :
                for item in sub :
                    box.append(item)
            
            print("box = " + str(box))
            
            boxes.append(box)
    
    return boxes
    
# givem 9 numbers, check to see if 1..9 are all in there
def checkGroup(group) :
    okay = True
    numbers = [1,2,3,4,5,6,7,8,9]
    
    for i in range(len(numbers)) :
        # check if in group
        for member in group :
            if (numbers[i] == member) :
                numbers[i] = 0
    
    for number in numbers :
        if number > 0 :
            okay = okay and False
    
    return okay