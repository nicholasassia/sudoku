import requests
from bs4 import BeautifulSoup
import time
import re

# Basic printing helper function to print out the 9x9 sudoku board
def printBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=" ")
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
        board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(0, 9):
            row = input(f"Input row {i+1} (use 0 for empty spaces): ")
            if len(row) != 9:
                print('Error. Please input correct rows using 0 for empty spaces.')
                return None
            board[i] = [int(x) for x in row]
        return board
    
    def scrape_from_web():
        url = input("Enter websudoku URL (e.g., https://www.websudoku.com/?level=1&set_id=***): ")
        return scrape_websudoku(url)
    
    # maybe i could put some ascii art or something here to make it fun, idk
    print('\033c', end='') # clears terminal, turn off if it messes with things
    print("Nicholas' Sudoku Solver!!!1!!1")
    print("1. Manual input")
    print("2. Scrape from web (websudoku)")
    choice = input("Choose an option (1/2): ")
    
    board = None
    if choice == '1':
        board = manual_input()
    elif choice == '2':
        board = scrape_from_web()
    else:
        print("Invalid choice, please choose 1 or 2.")
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
