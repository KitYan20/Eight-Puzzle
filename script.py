from eight_puzzle import *
# A python script to test out each search algorithm solving the Eight Puzzle 
""" process_file takes Three Input:
        1. a string filename name of a text file in which each line is a digit 
        string for an eight puzzle
        2. a string algorithm specifying which search algorithm should be used
        to solve the puzzles ('random', 'BFS', 'DFS', 'Greedy', or 'A*')
        3. a input parameter param that specifies whether to use a depth limit 
        searcher or a choice of heuristic function
"""
#BFS and DFS will use a depth limit while Greedy and A* will use a heuristic funtion
#5_moves.txt will be a default text file for the avg number of moves to solve each puzzle
#feel free to test out other txt file of Eight Puzzles and parameters for each search algorithm
#default depth limit for BFS and DFS is 5
#default heuristic function is h2 which return the number of tiles misplaced in the state by row and column
if __name__ == '__main__':
    while(True):
        print()
        print("Select a search algorithm to solve a puzzle")
        print("1: BFS (Breadth First Search)")
        print("2: DFS (Depth First Search)")
        print("3: Greedy")
        print("4: A*")
        print()
        number = input("Enter the number of the specified algorithm in:")
        number = int(number)
        print()
        if number == 1:
            print("Testing BFS ...")
            print(process_file('5_moves.txt','BFS',5))
            break
        elif number == 2:
            print("Testing DFS ...")
            print(process_file('5_moves.txt','DFS',5))
            break
        elif number == 3:
            print("Testing Greedy ...")
            print(process_file('5_moves.txt','Greedy',h2))
            break
        elif number == 4:
            print("Testing A* ...")
            print(process_file('5_moves.txt','A*',h2))
            break
        else:
            print("Oop! Wrong number typed in! Try again")
            
