# Advent of Code 2021
# Day x: Part I

import timeit


def whatever():
    """ whatever it does..."""


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day?.txt', "r") as f:
        data = f.read().splitlines()

    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")


