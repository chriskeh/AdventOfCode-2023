#!/usr/bin/env /usr/bin/python
import re

input_data_file = "part1.data"

def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    total = 0

    with open(input_data_file) as given_input_data:
        index = 1
        for line in given_input_data:
            line = line.strip()
            zuege_string = re.sub(r"Game .*:", "", line)
            zug_liste = zuege_string.split(";")

            red_max = 0
            green_max = 0
            blue_max = 0
            for zug in zug_liste:
                kugeln = zug.split(",")
                for kugel_string in kugeln:
                    kugel_string = kugel_string.strip()
                    kugel = kugel_string.split()
                    if kugel[1] == "red":
                        red_max = max(red_max, int(kugel[0]))
                    if kugel[1] == "green":
                        green_max = max(green_max, int(kugel[0]))
                    if kugel[1] == "blue":
                        blue_max = max(blue_max, int(kugel[0]))
            zug_power = red_max * green_max * blue_max
            total += zug_power


    print("Total: {}".format(total))


if __name__ == "__main__":
    main()
