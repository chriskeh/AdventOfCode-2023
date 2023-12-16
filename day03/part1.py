#!/usr/bin/env /usr/bin/python
import re

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of lists.
    """

    # For some reason getting substrings from strings with '.' fails.
    # So let's replace the "." with a "X" everywhere.
    dotted_line = ["X"] * 10
    input_data = []
    input_data.append("".join(dotted_line))
    with open(input_file) as given_input_data:
        for line in given_input_data:
            line = line.replace(".", "X").rstrip()
            input_data.append("X" + line + "X")
    input_data.append("".join(dotted_line))
    return input_data


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"
    zeilen = slurp_input(input_data_file)

    sum = 0
    zeilennummer = -1
    for zeile in zeilen:
        zeilennummer += 1
        index = 0
        while index < len(zeile):
            laenge = 1
            if zeile[index].isdecimal():
                laenge = 1
                while zeile[index + laenge].isdecimal():
                    laenge += 1

                # check char left of the number
                if zeile[index - 1] != "X":
                    if not zeile[index - 1].isdecimal():
                        sum += int(zeile[index:index + laenge])
                        print(int(zeile[index:index + laenge]))
                        index += laenge
                        continue

                # check char right of the number
                if zeile[index + laenge] != "X":
                    if not zeile[index + laenge].isdecimal():
                        sum += int(zeile[index:index + laenge])
                        print(int(zeile[index:index + laenge]))
                        index += laenge
                        continue

                # set links to the leftmost position to check
                # and rechts to the rightmost position to check
                links = index - 1
                rechts = index + laenge + 1

                # a pattern for the re.sub below to remove number from the string
                pattern = r'[0-9]'

                # check line above
                # above is the part of the above string that has to be checked. Starting one char left
                # and ending one char right of the number.
                # Be careful to not go beyond leftmost and rightmost border
                above = zeilen[zeilennummer - 1][links:rechts]
                # remove the fill character
                string_to_check = above.replace("X", "")
                # remove the digits
                string_to_check = re.sub(pattern, '', string_to_check)
                if string_to_check != "":
                    # If there is anything left, that means this number has to be counted
                    sum += int(zeile[index:index + laenge])
                    print(int(zeile[index:index + laenge]))
                    index += laenge
                    continue

                # The same for the line below
                below = zeilen[zeilennummer + 1][links:rechts]
                string_to_check = below.replace("X", "")
                string_to_check = re.sub(pattern, '', string_to_check)
                if string_to_check != "":
                    sum += int(zeile[index:index + laenge])
                    print(int(zeile[index:index + laenge]))
                    index += laenge
                    index += 1
                    continue
            index += laenge

    print("Total: {}".format(sum))


if __name__ == "__main__":
    main()
