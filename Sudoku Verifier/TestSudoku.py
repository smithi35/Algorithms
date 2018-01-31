from isSolved import *

first = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
second = [[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6],[7,7,7,7,7,7,7,7,7],[8,8,8,8,8,8,8,8,8],[9,9,9,9,9,9,9,9,9]]
third = [[1,1,1],[2,2,2],[3,3,3]]
oneD = [1]
twoD = [[1]]
justOnes = [[1,1,1,1,1,1,1,1,1]]
columnsOfOnes = [[1],[1],[1],[1],[1],[1],[1],[1],[1]]
hasATen = [[5,3,4,6,7,8,9,10,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]

def runTests() :
    print("Testing verifier functions")
    testFinishedFunction()
    testCheckRows()
    testGetColumns()
    testGetBoxes()
    testCheckGroup()

def testFinishedFunction() :
    print("Testing checkFinished function")
    
    assert(checkFinished(oneD) == False)
    assert(checkFinished(twoD) == False)
    assert(checkFinished(justOnes) == False)
    assert(checkFinished(columnsOfOnes) == False)
    assert(checkFinished(first) == True)
    assert(checkFinished(second) == True)
    assert(checkFinished(third) == False)
    assert(checkFinished(hasATen) == False)
    
    
def testCheckRows() :
    print("Testing checkRows function")
    assert(checkRows(first) == True)
    assert(checkRows(second) == False)
    assert(checkRows(third) == False)
    assert(checkRows(oneD) == False)
    assert(checkRows(twoD) == False)
    assert(checkRows(justOnes) == False)
    assert(checkRows(columnsOfOnes) == False)
    
def testGetColumns() :
    print("Testing getColumns");

    # if given a 1D array, getColumns should complain
    assert(getColumns(1) == None)
    
    columns = getColumns([1])
    assert(columns == None)
    
    # ensure it can handle square arrays that are not just 9x9
    columns = getColumns(third)
    assert(columns == [[1,2,3],[1,2,3],[1,2,3]])
    
    columns = getColumns([[1]])
    assert(columns == [[1]])
    
    # ensure it properly handles full puzzles
    columns = getColumns(first)
    for i in range(len(columns)) :
        array = []
        for item in columns[i]:
            array.append(i+1)
        assert(columns[i] == array)
        
    columns = getColumns(second)
    for i in range(len(columns)) :
        sub = []
        for j in range(len(second[i])) :
            sub.append(j+1)
        assert(sub == columns[i])

# getBoxes should be particularly picky over the input it receives        
def testGetBoxes() :
    print("Testing getBoxes function")
    
    assert(getBoxes([1]) == None)
    assert(getBoxes([1,1,1,1,1,1,1,1,1]) == None)
    assert(getBoxes([[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]) == None)
    assert(getBoxes([1,1,1,1,1,1,1,1,1,1,1,1]) == None)
    assert(getBoxes(1) == None)
    
    boxes = getBoxes(first)
    assert(boxes[0] == [1,2,3,1,2,3,1,2,3] and boxes[1] == [4,5,6,4,5,6,4,5,6] and boxes[2] == [7,8,9,7,8,9,7,8,9] and boxes[0] == boxes[3] == boxes[6] and boxes[1] == boxes[4] == boxes[7] and boxes[2] == boxes[5] == boxes[8])
    
    boxes = getBoxes(second)
    assert(boxes[4] == [4,4,4,5,5,5,6,6,6] and boxes[8] == [7,7,7,8,8,8,9,9,9])
    assert(boxes[1] == boxes[0] == boxes[2] and boxes[3] == boxes[4] == boxes[5] and boxes[6] == boxes[7] == boxes[8])
    
    
def testCheckGroup() :
    print("Testing checkGroup function")
    
    assert(checkGroup(1) == False)
    assert(checkGroup([1,2,3,4,5,6,7,8]) == False)
    assert(checkGroup([1,2,3,3,4,5,6,7,8]) == False)
    assert(checkGroup([1]) == False)
    assert(checkGroup([1,2,3,4,5,6,7,8,9]) == True)
    
runTests()