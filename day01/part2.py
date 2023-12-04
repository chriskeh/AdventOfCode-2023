#!/usr/bin/env /usr/bin/python36
import re

input_data_file = "part2.data"


def extract_number_from_line(line):
    digits = "".join(c for c in line if c.isdecimal())
    tens = int(digits[0])
    ones = int(digits[len(digits) - 1])
    number = 10 * tens + ones
    return number


def leftmost_literal_number_to_number(line):
    pos = []
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for nummer in number_words:
        stelle = line.find(nummer)
        if stelle == -1:
            stelle = 100000
        pos.append(stelle)

    first_literal_digit = pos.index(min(pos))
    line = re.sub(number_words[first_literal_digit], str(first_literal_digit), line)

    return(line)


def main():

    # uncomment the next line to read the input data from the test file
    input_data_file = "part2_test.data"

    with open(input_data_file) as given_data:
        total = 0
        for line in given_data:
            while True:
                correct_line = leftmost_literal_number_to_number(line)
                if line == correct_line:
                    break
                line = correct_line
            number = extract_number_from_line(correct_line)

            total += number

        print("Total: {}".format(total))


if __name__ == "__main__":
    main()
