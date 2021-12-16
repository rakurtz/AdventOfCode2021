# Advent of Code 2021
# Day 10: Part I

import timeit

def polymerize(input_list: list, insertion_map: dict):
    """ iterates through sample pairwise and inserts from the pair_insertion dict
        TODO: compare efficiency of global sample or return sample
    """
    offset = 0
    for index in range(len(input_list) - 1):
        corrected_index = index + offset
        pair = "".join(input_list[corrected_index:corrected_index + 2])
        input_list.insert(corrected_index + 1, insertion_map[pair])
        offset += 1

    return input_list


def count_elements(input_list: list):
    """ takes the sample and counts all occurrences
        returns a dict with {element: number}
    """
    elements = set(input_list)  # get unique elements
    counted = {}
    for element in elements:
        counted[element] = input_list.count(element)
    return counted


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day14.txt', "r") as f:
        data = f.read().splitlines()

    sample = list(data.pop(0))
    inerstion_map = {}
    for line in data[1:]:
        key, value = line.split(" -> ")
        inerstion_map[key] = value


    rounds_of_polymerization = 10
    for i in range(rounds_of_polymerization):
        polymerize(sample, inerstion_map)
        #print(i, len(sample))

    counted = count_elements(sample)
    most_common = max(counted, key=counted.get)
    rarest = min(counted, key=counted.get)
    result = counted[most_common] - counted[rarest]

    print(f"Part I: After {rounds_of_polymerization} rounds: most common element minus rarest element = {result}")




    stop = timeit.default_timer()
    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                              3247
    # Part II:
    # Part II took 0.001856500002759276 seconds

