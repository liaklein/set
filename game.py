from objects import *


def main():
    board = Board()
    while not board.isEmpty():
        board.display()
        userInput = raw_input("\nPlease Enter Set: ")
        print(userInput)

if __name__ == '__main__':
    main()
