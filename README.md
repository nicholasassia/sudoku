# sudoku

## **3x3 Sudoku Solver (NOW WITH WEB SCRAPING omg wow)**  
*(Only on [websudoku.com](https://websudoku.com))*  

This Python program solves a given 9x9 Sudoku puzzle using a simple backtracking algorithm.  

---

## **Instructions**  
There are **two ways** to input a puzzle: **manual input** and **web scraping**.  

### **1) Manual Input**  
The program will prompt you to enter each row of 9 values individually and solve the puzzle once all rows are provided.  

- You will be asked to input each row in this format:
  _ _ _ _ _ _ _ _ _ [1st row of given sudoku, leave blanks as 0's, **NO SPACES**]
- Repeat this 9 times for each row.  

### **2) Web Scraping**  
This method uses the `requests` package and `BeautifulSoup4` to retrieve and solve puzzles directly from **websudoku.com**.  

#### **Steps:**  
1. Run the program.  
2. Type in **2** when prompted (the web scrape option)
3. Copy the **link** from the websudoku.com puzzle page (*click on the **difficulty and number** buttom at the bottom of the puzzle to get the link*).  
4. Paste the **link** into the program when prompted.

---

## **Here is a short demonstration of the web scraping in action**  
![Sudoku Demo](https://github.com/user-attachments/assets/b042cb91-c611-431f-9fdf-4f35937d3347)  

