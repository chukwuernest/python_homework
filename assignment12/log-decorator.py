#TASK1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def takes_positional(*args):
    return True

@logger_decorator
def takes_keyword(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    takes_positional(1, 2, 3)
    takes_keyword(a=10, b=20)
    
    #TASK2
def type_decorator(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_decorator(str)
def return_int():
    return 5

@type_decorator(int)
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  
    
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  

#TASK3
import pandas as pd

df = pd.read_csv("../csv/employees.csv")


names = [f"{row['first_name']} {row['last_name']}" for idx, row in df.iterrows()]
print(names)


names_with_e = [name for name in names if 'e' in name.lower()]
print(names_with_e)

#TASK4
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join([char if char in guesses else "_" for char in secret_word])
        print(display)
        return "_" not in display

    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    hangman = make_hangman(secret_word)

    while True:
        guess = input("Guess a letter: ").lower()
        if hangman(guess):
            print("Congratulations! You've guessed the word.")
            break
           
#TASK5
import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        for start in range(0, len(self), 10):
            print(self.columns)
            print(super().iloc[start:start+10])

if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
    
#TASK6
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" "]*3 for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row, column = divmod(move_index, 3)
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        cat = all(self.board_array[i][j] != " " for i in range(3) for j in range(3))
        if cat:
            return (True, "Cat's Game.")
        win = False
        for i in range(3):
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True
        if win:
            winner = "X" if self.turn == "O" else "O"
            return (True, f"{winner} wins!")
        return (False, f"{self.turn}'s turn.")

if __name__ == "__main__":
    board = Board()
    while True:
        print(board)
        move = input(f"{board.turn}'s move: ").lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(e.message)
            continue
        game_over, message = board.whats_next()
        if game_over:
            print(board)
            print(message)
            break 