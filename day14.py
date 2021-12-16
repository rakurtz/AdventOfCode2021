# Advent of Code 2021
# Day 10: Part I

import timeit


def polymerize(sample: list, pair_insertion: dict):
    """ iterates through sample pairwise and inserts from the pair_insertion dict
        TODO: compare efficiency of global sample or return sample
    """
    offset = 0
    for index in range(len(sample)-1):
        corrected_index = index + offset
        pair = "".join(sample[corrected_index:corrected_index+2])
        sample.insert(corrected_index + 1, pair_insertion[pair])
        offset += 1

    return sample


def count_elements(sample: list):
    """ takes the sample and counts all occurrences
        returns a dict with {element: number}
    """
    elements = set(sample)  # get unique elements
    elements_count = {}
    for element in elements:
        elements_count[element] = sample.count(element)
    return elements_count


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day14.txt', "r") as f:
        data = f.read().splitlines()

    sample = list(data.pop(0))
    pair_insertion = {}
    for line in data[1:]:
        key, value = line.split("->")
        pair_insertion[key.strip()] = value.strip()

    rounds_of_polymerization = 13
    for i in range(rounds_of_polymerization):
        polymerize(sample, pair_insertion)
        #print(i, len(sample))

    element_count = count_elements(sample)
    most_common = max(element_count, key=element_count.get)
    rarest = min(element_count, key=element_count.get)
    result = element_count[most_common] - element_count[rarest]

    print(f"Part I: After {rounds_of_polymerization} rounds: most common element minus rarest element = {result}")




    stop = timeit.default_timer()
    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                              3247
    # Part II:
    # Part II took 0.001856500002759276 seconds

