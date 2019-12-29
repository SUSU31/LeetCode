class Solution:
    def isValidSudoku(self, board):
        for i in range(len(board)):
            flag = self.isValidblock(board[i])
            if flag == 0:
                return False
        for j in range(0,9):
            temp_block = []
            for i in range(0,9):
                temp_block.append(board[i][j])
            flag = self.isValidblock(temp_block)
            if flag == 0:
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                temp_block = []
                temp_block += board[i][j:j+3]
                temp_block += board[i+1][j:j + 3]
                temp_block += board[i+2][j:j + 3]
                flag = self.isValidblock(temp_block)
                if flag == 0:
                    return False
        return True

    def isValidblock(self, block):
        temp_list = []
        flag = 1
        for num in block:
            if num == '.':
                continue
            if num in temp_list:
                flag = 0
                break
            else:
                temp_list.append(num)
        return flag


if __name__ == '__main__':
    S= Solution()
    A = [
  ["5","3","6",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(S.isValidSudoku(A))