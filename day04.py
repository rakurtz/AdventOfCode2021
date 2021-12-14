# Advent of Code 2021
# Day 4: Part I + II
import timeit

with open('inputfiles/day4.txt', "r") as f:
    data = f.read().splitlines()

""" prepare data """
numbers, _, *boards_raw = data  # remove empty line between numbers and board's data
numbers = [int(number) for number in numbers.split(",")]
boards = [[int(number) for number in line.split()] for line in boards_raw if line]  # create continuing list of all boards


def mark_numbers_in_boards(to_mark):
    return [[number if not number == to_mark else "M" for number in row] for row in boards]


def check_bingo_horizontal(board_index):
    for row in boards[board_index:board_index + 5]:
        if row.count("M") == 5:
            return True


def check_bingo_vertical(board_index):
    vertical_count = [0] * 5
    for row in boards[board_index:board_index + 5]:
        for position, value in enumerate(row):      #
            if value == "M":
                vertical_count[position] += 1
        if 5 in vertical_count:
            return True


def sum_board_numbers(board_index):
    cleaned_board = ([number if not number == "M" else 0 for number in row] for row in boards[board_index:board_index + 5])
    board_sum = sum(sum(x) if isinstance(x, list) else x for x in cleaned_board)
    return board_sum


def solve_this():
    """ part 1 """
    global boards

    first_winner_board_sum = 0
    first_winning_number = 0

    order_of_winners = []
    last_winner_board = -1
    last_winning_number = -1

    while numbers:
        # while loop for every bingo number trough all boards
        actual_number = numbers.pop(0)
        boards = mark_numbers_in_boards(actual_number)  # mark all occurances in all boards with "M"

        for board_index in range(0, len(boards), 5):  # go boardwise
            if board_index in order_of_winners:
                # skip if board already got "bingoed" before
                continue

            elif check_bingo_horizontal(board_index) or check_bingo_vertical(board_index):
                # check if either vertical or horizontal there is new bingo...
                # if so, append in winner's history
                order_of_winners.append(board_index)

                # store the values: might be the last one, but only know in future loops
                last_winner_board = board_index
                last_winning_number = actual_number
                last_winner_board_sum = sum_board_numbers(board_index)

                # verbose...
                #print(last_winner_board, last_winning_number, last_winner_board_sum, last_winner_board_sum*last_winning_number)

                if len(order_of_winners) == 1:  # solution for Part 1
                    # make sure to save information of first bingo-board
                    first_winning_number = actual_number
                    first_winner_board_sum = last_winner_board_sum

                break

    solution_part1 = first_winner_board_sum * first_winning_number
    solution_part2 = last_winner_board_sum * last_winning_number
    return solution_part1, solution_part2


if __name__ == "__main__":
    start = timeit.default_timer()
    solution_part1, solution_part2 = solve_this()
    stop = timeit.default_timer()

    print(f"Part 1 = {solution_part1} \n"
          f"Part 2 = {solution_part2}")

    print(f"\nTook {stop - start} seconds to finish")



# Part 1: 60368 - Took 0.009730916004627943 seconds to finish
# Part 2: AoC says, the result for Part 2 is not correct. In test data it's correct. Dunno...