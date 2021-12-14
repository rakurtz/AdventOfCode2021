# Advent of Code 2021
# Day 10: Part I

import timeit


def check_line(syntax_line: str):
    """ parse each charakter and track all opening and closing characters
        corrupt lines are identified by a closing character which has another opening symbol as predecessor
        a valid closing character deletes it's opening partner from the list ( pop() )

        return 0 if not corrupt
        return score of corrupting character
    """
    opening = []

    for character in syntax_line:
        match character:
            case ("(" | "[" | "{" | "<"):   # all opening characters are just added to the list
                opening.append(character)

            case ")":
                if opening[-1] == "(":
                    opening.pop()
                else:
                    return 3

            case "]":
                if opening[-1] == "[":
                    opening.pop()
                else:
                    return 57

            case "}":
                if opening[-1] == "{":
                    opening.pop()
                else:
                    return 1197

            case ">":
                if opening[-1] == "<":
                    opening.pop()
                else:
                    return 25137

    return 0    # found nothing corrupt


def complete_line(syntax_line: str):
    """ reverse iterate through characters of lines and complete missing closing symbols
        by adding them to a list

        return list
    """
    completion = ""
    closing = []

    for character in syntax_line[::-1]:     # reverse iteration
        match character:
            case (")" | "]" | "}" | ">"):  # all closing characters are just added to the list
                closing.append(character)

            case "(":
                if closing and closing[-1] == ")":
                    closing.pop()
                else:
                    completion += ")"

            case "[":
                if closing and closing[-1] == "]":
                    closing.pop()
                else:
                    completion += "]"

            case "{":
                if closing and closing[-1] == "}":
                    closing.pop()
                else:
                    completion += "}"

            case "<":
                if closing and closing[-1] == ">":
                    closing.pop()
                else:
                    completion += ">"

    return completion


def calculate_score_part2(syntax_completion_line: str):
    """ calculate score of each line and return it """
    line_score = 0
    for character in syntax_completion_line:
        match character:
            case ")":
                line_score = (line_score * 5) + 1
            case "]":
                line_score = (line_score * 5) + 2
            case "}":
                line_score = (line_score * 5) + 3
            case ">":
                line_score = (line_score * 5) + 4

    return line_score


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day10.txt', "r") as f:
        syntax_input = f.read().splitlines()


    """ Part I 
        (including generating list of incomplete lines, which belongs to Part II) 
    """
    score = 0
    incomplete_syntax_lines = []

    for row, line in enumerate(syntax_input):
        return_code = check_line(line)
        if return_code > 0:
            score += return_code
        else:
            incomplete_syntax_lines.append(syntax_input[row])

    print(f"Part I: Score ist {score}")


    """ Part II 
    """
    completions = []
    scores = []

    for line in incomplete_syntax_lines:
        completions.append(complete_line(line))

    for line in completions:
        scores.append(calculate_score_part2(line))

    print(f"Part II: Middle score is {(sorted(scores)[(len(scores) // 2)])}")

    stop = timeit.default_timer()
    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                              442131
    # Part II:                         3646451424
    # All together:     Took 0.001856500002759276 seconds to finish
