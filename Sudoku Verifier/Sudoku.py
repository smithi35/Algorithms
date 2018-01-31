from isSolved import isSolved
from TestSudoku import runTests

def main() :
    runTests()
    print("The tests passed\n\n")
    
    # print("This one should fail")
    # puzzle = [[1]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should fail")
    # puzzle = [[1],[1],[1],[1],[1],[1],[1],[1],[1]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")

    # print("This one should fail")
    # puzzle = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should fail")
    # puzzle = [[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6],[7,7,7,7,7,7,7,7,7],[8,8,8,8,8,8,8,8,8],[9,9,9,9,9,9,9,9,9]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should pass")
    # puzzle = [[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should pass")
    # puzzle = [[8,2,7,1,5,4,3,9,6],[9,6,5,3,2,7,1,4,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should fail")
    # puzzle = [[8,2,7,1,5,4,3,9,6],[9,6,5,3,2,7,1,4,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,6,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should fail")
    # puzzle = [[5,3,4,6,7,8,9,10,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should fail")
    # puzzle = [[2,9,5,7,4,3,8,6,1],[4,3,1,8,6,5,9,2,7],[8,7,6,1,9,2,5,4,3],[3,8,7,4,5,9,2,1,6],[6,1,2,3,8,7,4,9,5],[5,4,9,2,1,6,7,3,8],[7,6,3,5,3,4,1,8,9],[9,2,8,6,7,1,3,5,4],[1,5,4,9,3,8,6,7,2]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This one should pass")
    # puzzle = [[1,5,2,4,8,9,3,7,6],[7,3,9,2,5,6,8,4,1],[4,6,8,3,7,1,2,9,5],[3,8,7,1,2,4,6,5,9],[5,9,1,7,6,3,4,2,8],[2,4,6,8,9,5,7,1,3],[9,1,4,6,3,7,5,8,2],[6,2,5,9,4,8,1,3,7],[8,7,3,5,1,2,9,6,4]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    # print("This, the original puzzle from the assignment, should pass")
    # puzzle = [[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    # printPuzzle(puzzle)
    # print("Solved? " + str(isSolved(puzzle)) + "\n")
    
    print("I switched the rows and columns to see if it still passes")
    puzzle = [[5,6,1,8,4,7,9,2,3],[3,7,9,5,2,1,6,8,4],[4,2,8,9,6,3,1,7,5],[6,1,3,7,8,9,5,4,2],[7,9,4,6,5,2,3,1,8],[8,5,2,1,3,4,7,9,6],[9,3,5,4,7,8,2,6,1],[1,4,6,2,9,5,8,3,7],[2,8,7,3,1,6,4,5,9]]
    printPuzzle(puzzle)
    print("Solved? " + str(isSolved(puzzle)) + "\n")

def printPuzzle(puzzle) :
    print("Printing Puzzle: ")
    for sub in puzzle :
        print(sub)
main()