class game:
    
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    position_column = 0
    position_row = 0
    winner = None
    count = 0

    def __init__(self, player):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.player = player
        self.position_column = self.position_column
        self.position_row = self.position_row

    def print_board(self):
        print(" _ ", "_", " _ ", end="")

        for x in range(3):
            print("\n", end="")
            for i in range(3):
                print("|" + game.board[x][i] + "|", end="")

    def inputposition(self):
        game.count += 1
        self.position_column = int(
            input("\n" + self.player + " Please input column position: ")
        )
        while True:
            if (
                self.position_column != 0
                and self.position_column != 1
                and self.position_column != 2
            ):
                print("Please try again.")

            else:
                break
            self.position_column = int(
                input("\n" + self.player + " Please input column position: ")
            )

        self.position_row = int(input(self.player + " Please input row position: "))

        while True:
            if (
                self.position_row != 0
                and self.position_row != 1
                and self.position_row != 2
            ):
                print("Please try again.")

            else:
                break
            self.position_row = int(input(self.player + " Please input row position: "))

        while True:
            if game.board[self.position_column][self.position_row] != "_":
                print("Please try again.")

            else:
                break

            self.position_column = int(
                input("\n" + self.player + " Please input column position: ")
            )
            self.position_row = int(input(self.player + " Please input row position: "))

        if self == Player1:
            self.board[self.position_column][self.position_row] = "x"
            game.board[self.position_column][self.position_row] = "x"

        else:
            self.board[self.position_column][self.position_row] = "O"
            game.board[self.position_column][self.position_row] = "O"

    def check(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "_":
                game.winner = self.player

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "_":
                game.winner = self.player

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "_":
            game.winner = self.player

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "_":
            game.winner = self.player

    def check_winner():
        if game.winner != None:
            print("\n{} is the winner!".format(game.winner))

        if game.count == 9:
            print("\ndraw")

        else:
            return 0


Player1 = game("Player1")
Player2 = game("Player2")
game.print_board(Player1)

for i in range(1, 10):
    if game.winner:
        break

    if i % 2 == 1:
        Player1.inputposition()
        Player1.print_board()
        Player1.check()

    else:
        Player2.inputposition()
        Player2.print_board()
        Player2.check()

    game.check_winner()
