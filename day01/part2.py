#!/usr/bin/env /usr/bin/python
input_data_file = "part2.data"

def get_leftmost_digit_from_line(line):
    # Walk over the string from left to right.
    # If the character is a digit, return it as int()
    # If not, check if this is the start of a written digit. If one is found, return it as int()
    # If we didn't find any, return -1
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    index = 0
    while index < len(line):
        # If this is a digit, return it right away
        if line[index].isdecimal():
            return int(line[index])
        # No digit, so let's see if we found a digit as written text
        text_to_check = line[index:]
        number = 0
        while number < 10:
            if text_to_check.startswith(number_words[number]):
                return number
            number += 1
        index += 1
    return -1

def get_rightmost_digit_from_line(line):
    # Walk over the string from right to left.  The idea is the same as in get_leftmost_digit_from_line()
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    index = len(line) - 1
    while index >= 0:
        if line[index].isdecimal():
            return int(line[index])
        text_to_check = line[index:]
        number = 0
        while number < 10:
            if text_to_check.startswith(number_words[number]):
                return number
            number += 1
        index -= 1
    return -1


def main():
    # uncomment the next line to read the input data from the test file

    # input_data_file = "part2_test.data"

    total = 0
    with open(input_data_file) as given_data:
        for line in given_data:
            zehner = get_leftmost_digit_from_line(line.rstrip())
            einser = get_rightmost_digit_from_line(line.rstrip())
            total += 10 * zehner + einser

        print("Total: {}".format(total))


if __name__ == "__main__":
    main()
