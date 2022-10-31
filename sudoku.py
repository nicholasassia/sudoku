board = [[],[],[],[],[],[],[],[],[]]

def makeBoard():
    for i in range(0,9):
        row = input(f"input row {i+1}: ")
        if (len(row) != 9):
            print('error. please input correct rows using 0 for empty spaces.')
            break
        board[i] = [int(x) for x in row]

makeBoard()

''' WEB DATA FOR SCRAPE (when i figure it out)
websudoku.com is the domain
html path -> <tbody><tr><td class="g0" id="c00"><input class="d0" size="2" autocomplete="off" name="ea0ux11" maxlength="1" onblur="j8(this)" id="f00"></td><td class="f0" id="c10"><input class="d0" size="2" autocomplete="off" name="ea0ux21" maxlength="1" onblur="j8(this)" id="f10"></td><td class="f0" id="c20"><input class="s0" size="2" autocomplete="off" name="sea0ux31" readonly="" value="1" id="f20"></td><td class="g0" id="c30"><input class="d0" size="2" autocomplete="off" name="ea0ux41" maxlength="1" onblur="j8(this)" id="f30"></td><td class="f0" id="c40"><input class="d0" size="2" autocomplete="off" name="ea0ux51" maxlength="1" onblur="j8(this)" id="f40"></td><td class="f0" id="c50"><input class="d0" size="2" autocomplete="off" name="ea0ux61" maxlength="1" onblur="j8(this)" id="f50"></td><td class="g0" id="c60"><input class="d0" size="2" autocomplete="off" name="ea0ux71" maxlength="1" onblur="j8(this)" id="f60"></td><td class="f0" id="c70"><input class="d0" size="2" autocomplete="off" name="ea0ux81" maxlength="1" onblur="j8(this)" id="f70"></td><td class="f0" id="c80"><input class="s0" size="2" autocomplete="off" name="sea0ux91" readonly="" value="2" id="f80"></td></tr><tr><td class="e0" id="c01"><input class="s0" size="2" autocomplete="off" name="sea0ux12" readonly="" value="3" id="f01"></td><td class="c0" id="c11"><input class="d0" size="2" autocomplete="off" name="ea0ux22" maxlength="1" onblur="j8(this)" id="f11"></td><td class="c0" id="c21"><input class="d0" size="2" autocomplete="off" name="ea0ux32" maxlength="1" onblur="j8(this)" id="f21"></td><td class="e0" id="c31"><input class="d0" size="2" autocomplete="off" name="ea0ux42" maxlength="1" onblur="j8(this)" id="f31"></td><td class="c0" id="c41"><input class="s0" size="2" autocomplete="off" name="sea0ux52" readonly="" value="4" id="f41"></td><td class="c0" id="c51"><input class="d0" size="2" autocomplete="off" name="ea0ux62" maxlength="1" onblur="j8(this)" id="f51"></td><td class="e0" id="c61"><input class="s0" size="2" autocomplete="off" name="sea0ux72" readonly="" value="6" id="f61"></td><td class="c0" id="c71"><input class="d0" size="2" autocomplete="off" name="ea0ux82" maxlength="1" onblur="j8(this)" id="f71"></td><td class="c0" id="c81"><input class="s0" size="2" autocomplete="off" name="sea0ux92" readonly="" value="8" id="f81"></td></tr><tr><td class="e0" id="c02"><input class="d0" size="2" autocomplete="off" name="ea0ux13" maxlength="1" onblur="j8(this)" id="f02"></td><td class="c0" id="c12"><input class="s0" size="2" autocomplete="off" name="sea0ux23" readonly="" value="2" id="f12"></td><td class="c0" id="c22"><input class="d0" size="2" autocomplete="off" name="ea0ux33" maxlength="1" onblur="j8(this)" id="f22"></td><td class="e0" id="c32"><input class="s0" size="2" autocomplete="off" name="sea0ux43" readonly="" value="5" id="f32"></td><td class="c0" id="c42"><input class="d0" size="2" autocomplete="off" name="ea0ux53" maxlength="1" onblur="j8(this)" id="f42"></td><td class="c0" id="c52"><input class="d0" size="2" autocomplete="off" name="ea0ux63" maxlength="1" onblur="j8(this)" id="f52"></td><td class="e0" id="c62"><input class="d0" size="2" autocomplete="off" name="ea0ux73" maxlength="1" onblur="j8(this)" id="f62"></td><td class="c0" id="c72"><input class="s0" size="2" autocomplete="off" name="sea0ux83" readonly="" value="1" id="f72"></td><td class="c0" id="c82"><input class="d0" size="2" autocomplete="off" name="ea0ux93" maxlength="1" onblur="j8(this)" id="f82"></td></tr><tr><td class="g0" id="c03"><input class="d0" size="2" autocomplete="off" name="ea0ux14" maxlength="1" onblur="j8(this)" id="f03"></td><td class="f0" id="c13"><input class="d0" size="2" autocomplete="off" name="ea0ux24" maxlength="1" onblur="j8(this)" id="f13"></td><td class="f0" id="c23"><input class="d0" size="2" autocomplete="off" name="ea0ux34" maxlength="1" onblur="j8(this)" id="f23"></td><td class="g0" id="c33"><input class="d0" size="2" autocomplete="off" name="ea0ux44" maxlength="1" onblur="j8(this)" id="f33"></td><td class="f0" id="c43"><input class="s0" size="2" autocomplete="off" name="sea0ux54" readonly="" value="2" id="f43"></td><td class="f0" id="c53"><input class="s0" size="2" autocomplete="off" name="sea0ux64" readonly="" value="6" id="f53"></td><td class="g0" id="c63"><input class="d0" size="2" autocomplete="off" name="ea0ux74" maxlength="1" onblur="j8(this)" id="f63"></td><td class="f0" id="c73"><input class="d0" size="2" autocomplete="off" name="ea0ux84" maxlength="1" onblur="j8(this)" id="f73"></td><td class="f0" id="c83"><input class="d0" size="2" autocomplete="off" name="ea0ux94" maxlength="1" onblur="j8(this)" id="f83"></td></tr><tr><td class="e0" id="c04"><input class="d0" size="2" autocomplete="off" name="ea0ux15" maxlength="1" onblur="j8(this)" id="f04"></td><td class="c0" id="c14"><input class="s0" size="2" autocomplete="off" name="sea0ux25" readonly="" value="6" id="f14"></td><td class="c0" id="c24"><input class="s0" size="2" autocomplete="off" name="sea0ux35" readonly="" value="7" id="f24"></td><td class="e0" id="c34"><input class="d0" size="2" autocomplete="off" name="ea0ux45" maxlength="1" onblur="j8(this)" id="f34"></td><td class="c0" id="c44"><input class="d0" size="2" autocomplete="off" name="ea0ux55" maxlength="1" onblur="j8(this)" id="f44"></td><td class="c0" id="c54"><input class="d0" size="2" autocomplete="off" name="ea0ux65" maxlength="1" onblur="j8(this)" id="f54"></td><td class="e0" id="c64"><input class="s0" size="2" autocomplete="off" name="sea0ux75" readonly="" value="9" id="f64"></td><td class="c0" id="c74"><input class="s0" size="2" autocomplete="off" name="sea0ux85" readonly="" value="8" id="f74"></td><td class="c0" id="c84"><input class="d0" size="2" autocomplete="off" name="ea0ux95" maxlength="1" onblur="j8(this)" id="f84"></td></tr><tr><td class="e0" id="c05"><input class="d0" size="2" autocomplete="off" name="ea0ux16" maxlength="1" onblur="j8(this)" id="f05"></td><td class="c0" id="c15"><input class="d0" size="2" autocomplete="off" name="ea0ux26" maxlength="1" onblur="j8(this)" id="f15"></td><td class="c0" id="c25"><input class="d0" size="2" autocomplete="off" name="ea0ux36" maxlength="1" onblur="j8(this)" id="f25"></td><td class="e0" id="c35"><input class="s0" size="2" autocomplete="off" name="sea0ux46" readonly="" value="9" id="f35"></td><td class="c0" id="c45"><input class="s0" size="2" autocomplete="off" name="sea0ux56" readonly="" value="7" id="f45"></td><td class="c0" id="c55"><input class="d0" size="2" autocomplete="off" name="ea0ux66" maxlength="1" onblur="j8(this)" id="f55"></td><td class="e0" id="c65"><input class="d0" size="2" autocomplete="off" name="ea0ux76" maxlength="1" onblur="j8(this)" id="f65"></td><td class="c0" id="c75"><input class="d0" size="2" autocomplete="off" name="ea0ux86" maxlength="1" onblur="j8(this)" id="f75"></td><td class="c0" id="c85"><input class="d0" size="2" autocomplete="off" name="ea0ux96" maxlength="1" onblur="j8(this)" id="f85"></td></tr><tr><td class="g0" id="c06"><input class="d0" size="2" autocomplete="off" name="ea0ux17" maxlength="1" onblur="j8(this)" id="f06"></td><td class="f0" id="c16"><input class="s0" size="2" autocomplete="off" name="sea0ux27" readonly="" value="4" id="f16"></td><td class="f0" id="c26"><input class="d0" size="2" autocomplete="off" name="ea0ux37" maxlength="1" onblur="j8(this)" id="f26"></td><td class="g0" id="c36"><input class="d0" size="2" autocomplete="off" name="ea0ux47" maxlength="1" onblur="j8(this)" id="f36"></td><td class="f0" id="c46"><input class="d0" size="2" autocomplete="off" name="ea0ux57" maxlength="1" onblur="j8(this)" id="f46"></td><td class="f0" id="c56"><input class="s0" size="2" autocomplete="off" name="sea0ux67" readonly="" value="7" id="f56"></td><td class="g0" id="c66"><input class="d0" size="2" autocomplete="off" name="ea0ux77" maxlength="1" onblur="j8(this)" id="f66"></td><td class="f0" id="c76"><input class="s0" size="2" autocomplete="off" name="sea0ux87" readonly="" value="5" id="f76"></td><td class="f0" id="c86"><input class="d0" size="2" autocomplete="off" name="ea0ux97" maxlength="1" onblur="j8(this)" id="f86"></td></tr><tr><td class="e0" id="c07"><input class="s0" size="2" autocomplete="off" name="sea0ux18" readonly="" value="9" id="f07"></td><td class="c0" id="c17"><input class="d0" size="2" autocomplete="off" name="ea0ux28" maxlength="1" onblur="j8(this)" id="f17"></td><td class="c0" id="c27"><input class="s0" size="2" autocomplete="off" name="sea0ux38" readonly="" value="2" id="f27"></td><td class="e0" id="c37"><input class="d0" size="2" autocomplete="off" name="ea0ux48" maxlength="1" onblur="j8(this)" id="f37"></td><td class="c0" id="c47"><input class="s0" size="2" autocomplete="off" name="sea0ux58" readonly="" value="3" id="f47"></td><td class="c0" id="c57"><input class="d0" size="2" autocomplete="off" name="ea0ux68" maxlength="1" onblur="j8(this)" id="f57"></td><td class="e0" id="c67"><input class="d0" size="2" autocomplete="off" name="ea0ux78" maxlength="1" onblur="j8(this)" id="f67"></td><td class="c0" id="c77"><input class="d0" size="2" autocomplete="off" name="ea0ux88" maxlength="1" onblur="j8(this)" id="f77"></td><td class="c0" id="c87"><input class="s0" size="2" autocomplete="off" name="sea0ux98" readonly="" value="1" id="f87"></td></tr><tr><td class="i0" id="c08"><input class="s0" size="2" autocomplete="off" name="sea0ux19" readonly="" value="6" id="f08"></td><td class="h0" id="c18"><input class="d0" size="2" autocomplete="off" name="ea0ux29" maxlength="1" onblur="j8(this)" id="f18"></td><td class="h0" id="c28"><input class="d0" size="2" autocomplete="off" name="ea0ux39" maxlength="1" onblur="j8(this)" id="f28"></td><td class="i0" id="c38"><input class="d0" size="2" autocomplete="off" name="ea0ux49" maxlength="1" onblur="j8(this)" id="f38"></td><td class="h0" id="c48"><input class="d0" size="2" autocomplete="off" name="ea0ux59" maxlength="1" onblur="j8(this)" id="f48"></td><td class="h0" id="c58"><input class="d0" size="2" autocomplete="off" name="ea0ux69" maxlength="1" onblur="j8(this)" id="f58"></td><td class="i0" id="c68"><input class="s0" size="2" autocomplete="off" name="sea0ux79" readonly="" value="7" id="f68"></td><td class="h0" id="c78"><input class="d0" size="2" autocomplete="off" name="ea0ux89" maxlength="1" onblur="j8(this)" id="f78"></td><td class="h0" id="c88"><input class="d0" size="2" autocomplete="off" name="ea0ux99" maxlength="1" onblur="j8(this)" id="f88"></td></tr></tbody>
//*[@id="puzzle_grid"]/tbody/tr[1] xpath
document.querySelector("#puzzle_grid > tbody") js path
/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/div[2]/table/tbody xpath full
boxes with a readonly value have a number in space; boxes without this attribute are a 0 (have onblur attribute)
'''

def printBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=" ")
        print()

def isPossible(board, row, col, val):
    for j in range(0, 9):
        if board[row][j] == val:
            return False

    for i in range(0, 9):
        if board[i][col] == val:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[startRow+i][startCol+j] == val:
                return False
    return True

def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for val in range(1, 10):
                    if isPossible(board, i, j, val):
                        board[i][j] = val
                        solve()
                        board[i][j] = 0
                return
    printBoard(board)

solve()

'''
SAMPLE RUN:
input row 1: 030010000
input row 2: 400000082
input row 3: 001007003
input row 4: 000209004
input row 5: 002000500
input row 6: 100405000
input row 7: 800500700
input row 8: 370000005
input row 9: 000080090

6 3 5 8 1 2 4 7 9 
4 9 7 3 5 6 1 8 2 
2 8 1 9 4 7 6 5 3 
7 5 8 2 6 9 3 1 4 
9 4 2 1 3 8 5 6 7 
1 6 3 4 7 5 9 2 8 
8 2 6 5 9 4 7 3 1 
3 7 9 6 2 1 8 4 5 
5 1 4 7 8 3 2 9 6 
'''
