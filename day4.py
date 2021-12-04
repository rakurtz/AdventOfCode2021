# Advent of Code 2021
# Day 4: Part I

import timeit

with open('inputfiles/day4.txt', "r") as f:
    data = f.read().splitlines()

""" prepare data """
numbers, _, *boards_raw = data  # remove first empty line
numbers = [int(number) for number in numbers.split(",")]
boards = [[int(number) for number in line.split()] for line in boards_raw if line]  # create continuing list of all boards, differ them later by row % 5


def part1():
    """ first part of puzzle"""
    global boards
    global numbers

    def mark_numbers_in_boards(to_mark):
        return [[number if not number == to_mark else "M" for number in row] for row in boards]

    def check_bingo_horizontal(board_index):
        for row in boards[board_index : board_index + 5]:
            if row.count("M") == 5:
                return True

    def check_bingo_vertical(board_index):
        for row in boards[board_index : board_index + 5]:
            vertical_count = [0] * 5
            for position, value in enumerate(row):      #
                if value == "M":
                    vertical_count[position] += 1
            if 5 in vertical_count:
                return True

    def sum_unmarked(board_index):
        cleaned_board = ([number if not number == "M" else 0 for number in row] for row in boards[board_index : board_index + 5])
        board_sum = sum(sum(x) if isinstance(x, list) else x for x in cleaned_board)
        return board_sum



    """ sequential code starts here """
    bingo = False
    winner_board_sum = 0
    winning_number = 0
    while numbers and not bingo:
        actual_number = numbers.pop(0)
        boards = mark_numbers_in_boards(actual_number)

        for board_index in range(0, len(boards), 5):  # go boardwise
            if check_bingo_horizontal(board_index) or check_bingo_vertical(board_index):
                bingo = True
                winning_number = actual_number
                winner_board_sum = sum_unmarked(board_index)
                break

        if bingo:
            break

    return winner_board_sum * winning_number


def part2():
    """ second part of puzzle"""
    pass


if __name__ == "__main__":
    start = timeit.default_timer()
    print(f"Part 1: {part1()}")
    print(f"Part 1: {part2()}")
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")



# Part 1: 60368 - Took 0.009730916004627943 seconds to finish