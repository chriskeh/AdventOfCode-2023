#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    my_answers = []
    this_answer = set()

    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                my_answers.append(this_answer)
                break

            line = line.strip()
            if line != "":
                for answer in line:
                    this_answer.add(answer)
            else:
                # The line is empty.
                # Prepare for next block: Add this_passport to the list, empty this_passport and increase passport_index.
                my_answers.append(this_answer)
                this_answer = set()
                continue

    return my_answers


def extract_number_from_line(line):
    digits = "".join(c for c in line if c.isdecimal())
    tens = int(digits[0])
    ones = int(digits[len(digits) - 1])
    number = 10 * tens + ones
    return number


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    with open(input_data_file) as given_data:
        total = 0
        for line in given_data:
            number = extract_number_from_line(line)
            total += number
        print("Total: {}".format(total))


if __name__ == "__main__":
    main()
