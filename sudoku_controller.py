"""
Juan-Taner Allerborn
PP
Sudoku Controller
13.09.2022
"""


class SudokuController():
    DIFFICULT_SETTINGS = ["Beginner", "Medium", "Average"]

    def __init__(self):
        self.difficulty = ""

    def set_difficulty(self):
        print("Welcome to the Sudoku Game")
        print("With what difficulty do you want tom play?")
        settings = False

        while settings != True:
            user_input = str(input("Beginner, Medium or Average?: "))
            user_input = user_input.capitalize()
            if user_input in SudokuController.DIFFICULT_SETTINGS:
                self.difficulty = user_input
                settings = True
            else:
                print("Falsche Eingabe: Versuchen Sie es erneut!")

    def __str__(self):
        return f"You choosed {self.difficulty}"


if __name__ == '__main__':
    player = SudokuController()
    player.set_difficulty()
    print(player)
