import requests
from bs4 import BeautifulSoup
import time
import re

# Basic printing helper function to print out the 9x9 sudoku board
def printBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ") #uses dots for blank spaces, the 0's were a bit hard on the eyes
        print()

# Checks if the board is still possible to solve at the given state
def isPossible(board, row, col, val):
    # checks rows
    for j in range(0, 9):
        if board[row][j] == val:
            return False
    # columns
    for i in range(0, 9):
        if board[i][col] == val:
            return False
    # 3x3 boxes
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[startRow+i][startCol+j] == val:
                return False
    return True

# Pretty simple backtracking method of brute-forcing solution
def solve(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for val in range(1, 10):
                    if isPossible(board, i, j, val):
                        board[i][j] = val
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# web scraping function with subdomain handling using soup and requests
def scrape_websudoku(url):
    try:
        if "websudoku.com" in url and not re.search(r"^https?://(east|west)\.websudoku\.com", url):
            # extract level and set_id from the URL
            level_match = re.search(r"level=(\d+)", url)
            set_id_match = re.search(r"set_id=(\d+)", url)
            
            level = level_match.group(1) if level_match else "1"
            set_id = set_id_match.group(1) if set_id_match else ""
            
            # websudoku hosts their puzzle pages on either east.websudoku or west.websudoku, so this just checks both
            subdomains = ["east", "west"]
            for subdomain in subdomains:
                test_url = f"http://{subdomain}.websudoku.com/?level={level}"
                if set_id:
                    test_url += f"&set_id={set_id}"
                
                print(f"Trying URL: {test_url}")
                response = requests.get(test_url)
                if response.status_code == 200 and "puzzle_grid" in response.text:
                    url = test_url
                    print(f"Successfully found puzzle at: {url}")
                    break
            else:
                print("Could not find puzzle on either subdomain. Trying the original URL.")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # initialize empty board
        board = [[0 for _ in range(9)] for _ in range(9)]
        
        # get the puzzle grid
        puzzle_grid = soup.select_one("#puzzle_grid")
        if not puzzle_grid:
            print("Couldn't find puzzle grid.")
            return None
        
        rows = puzzle_grid.find_all('tr')
        for i, row in enumerate(rows):
            cells = row.find_all('td')
            for j, cell in enumerate(cells):
                input_elem = cell.find('input')
                if input_elem:
                    # if it has read-only attribute, it's a pre-filled cell
                    if input_elem.has_attr('readonly'):
                        value = input_elem.get('value')
                        if value and value.isdigit():
                            board[i][j] = int(value)
                    # otherwise it's an empty cell (0)
                    else:
                        board[i][j] = 0
        
        return board
    except Exception as e:
        print(f"Error scraping WebSudoku: {e}")
        return None

# putting it all together in main
def main():
    def manual_input():
        print("\nEnter each row as 9 digits (use 0 for empty spaces).")
        board = [[0 for _ in range(9)] for _ in range(9)] # initialize 9x9 0 matrix
        
        for i in range(9):
            while True:  # keep asking until valid input
                print(f"\nCurrent board (Row {i+1}/9):")
                printBoard(board)
                
                row = input(f"Input row {i+1}: ").strip()
                
                if len(row) != 9 or not row.isdigit():
                    print("Error: Row must be 9 digits (0-9). Try again.")
                    continue
                
                # update board
                board[i] = [int(x) for x in row]
                break

        return board
    
    def scrape_from_web():
        url = input("\nEnter websudoku URL (e.g., https://www.websudoku.com/?level=1&set_id=***): ")
        return scrape_websudoku(url)

    def scrape_number():
        while True:
            diffInput = input("\nEnter puzzle difficulty (1=Easy, 2=Medium, 3=Hard, 4=Evil): ").lower()
            if diffInput in ("1", "easy"):
                diff = 1
                break
            elif diffInput in ("2", "medium"):
                diff = 2
                break
            elif diffInput in ("3", "hard"):
                diff = 3
                break
            elif diffInput in ("4", "evil"):
                diff = 4
                break
            else:
                print("\nerror, invalid input. please try again\n")

        while True:
            puzzle_num_input = input("Enter puzzle number: ").strip()
            puzzle_num_str = re.sub(r"[^\d]", "", puzzle_num_input) # regex to account for commas or someting..

            if puzzle_num_str: # if they actually put a numbah
                puzzle_num = int(puzzle_num_str)
                break
            else:
                print("invalid input. please enter a number.")
        
        url = "https://www.websudoku.com/?level=%d&set_id=%d" % (diff, puzzle_num)
        return scrape_websudoku(url)
        
    
    # maybe i could put some ascii art or something here to make it fun, idk
    print('\033c', end='') # clears terminal, turn off if it messes with things
    print("Nicholas' Sudoku Solver!!!1!!1")
    print("1. Manual input")
    print("2. Scrape from web (websudoku)")
    print("3. Difficulty and puzzle number (also websudoku)")
    choice = input("\nChoose an option (1/2/3): ")
    
    board = None
    if choice == '1':
        board = manual_input()
    elif choice == '2':
        board = scrape_from_web()
    elif choice == '3':
        board = scrape_number()
    else:
        print("Invalid choice, please choose 1,2 or 3.")
        return
    
    if board:
        print("\nOriginal board:")
        printBoard(board)
        
        solved_board = [row[:] for row in board]
        
        start_time = time.time()
        if solve(solved_board):
            end_time = time.time()
            print("\nSolution found in {:.3f} seconds:".format(end_time - start_time))
            printBoard(solved_board)
        else:
            print("\nNo solution exists.")

if __name__ == "__main__":
    main()
