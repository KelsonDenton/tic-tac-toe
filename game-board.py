board = [" "] * 9


def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n' +
          '----------' + '\n' +
          board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n' +
          '----------' + '\n' +
          board[6] + ' | ' + board[7] + ' | ' + board[8])


if __name__ == "__main__":
    print_board()
