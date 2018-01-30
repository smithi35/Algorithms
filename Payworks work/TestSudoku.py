from isSolved import *

def runTests() :
    checkFinishedFunction()
    checkGetColumns()
    checkGetBoxes()

def checkFinishedFunction() :
    print("checkFinished determines whether the array contains 9 inner arrays of 9 items")
    
    assert(checkFinished([1]) == False)
    assert(checkFinished([[1]]) == False)
    assert(checkFinished([[1,1,1,1,1,1,1,1,1]]) == False)
    assert(checkFinished([[1],[1],[1],[1],[1],[1],[1],[1],[1]]) == False)
    assert(checkFinished([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]) == True)
    
    return True
    
def checkGetColumns() :
    print("getColumns should return 9 arrays representing the columns of the sudoku puzzle");
    
    
    
    return True
    
def checkGetBoxes() :
    return True
    