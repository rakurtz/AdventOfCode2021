# Advent of Code 2021
# Day 3: Part I + II

import timeit

with open('inputfiles/day3.txt', "r") as f:
    data = f.read().splitlines()


def part1_string_based():
    """ first part of puzzle """
    count_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma_rate = ""
    epsilon_rate = ""

    for number_string in data:
        for position, digit in enumerate(number_string):
            if digit == "1":
                count_ones[position] += 1

    for count in count_ones:
        if count > len(data) / 2:   # more than half of the numbers have digit 1 here
            gamma_rate += "1"
            epsilon_rate += "0"
        else:                       # here more of them are digit 0
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)



def part2_string_based():
    """ second part of puzzle"""
    oxygen_generator = data
    co2_scrubber = data

    def counter_for_position(input_data, position, by_value: str):
        """ returns most common digit at given position """
        x = 0
        for string_number in input_data:
            if string_number[position] == by_value:
                x += 1
        return x

    def reduce_input(input_data, position, only_keep_value: str):
        reduced_data = []
        for string_number in input_data:
            if string_number[position] == only_keep_value:
                reduced_data.append(string_number)
        return reduced_data


    # reduce oxygen_generator
    for position in range(len(data[0])):
        if len(oxygen_generator) == 1:
            break

        count = counter_for_position(oxygen_generator, position, "1")
        if count >= len(oxygen_generator) / 2:
            oxygen_generator = reduce_input(oxygen_generator, position, "1")
        else:
            oxygen_generator = reduce_input(oxygen_generator, position, "0")


    # reduce co2 scrubber
    for position in range(len(data[0])):
        if len(co2_scrubber) == 1:
            break
        count = counter_for_position(co2_scrubber, position, "0")
        if count <= len(co2_scrubber) / 2:
            co2_scrubber = reduce_input(co2_scrubber, position, "0")
        else:
            co2_scrubber = reduce_input(co2_scrubber, position, "1")


    # final result
    return int(oxygen_generator[0], 2) * int(co2_scrubber[0], 2)


if __name__ == "__main__":
    start = timeit.default_timer()
    print(f"Part 1: {part1_string_based()}")
    print(f"Part 2: {part2_string_based()}")
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")

    # Part I:   1071734 - Took 0.0006397090037353337 seconds to finish
    # Part II:  6124992 - Took 0.000317458005156368 seconds to finish



