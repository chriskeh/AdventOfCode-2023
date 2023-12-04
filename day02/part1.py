#!/usr/bin/env /usr/bin/python
import re

input_data_file = "part1.data"

def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    total = 0
    red_load = 12
    green_load = 13
    blue_load = 14

    with open(input_data_file) as given_input_data:
        index = 1
        for line in given_input_data:
            impossible = False
            line = line.strip()
            zuege_string = re.sub(r"Game .*:", "", line)
            zug_liste = zuege_string.split(";")
            for zug in zug_liste:
                kugeln = zug.split(",")
                for kugel_string in kugeln:
                    kugel_string = kugel_string.strip()
                    kugel = kugel_string.split()
                    if kugel[1] == "red":
                        if int(kugel[0]) > red_load:
                            impossible = True
                            break
                    if kugel[1] == "green":
                        if int(kugel[0]) > green_load:
                            impossible = True
                            break
                    if kugel[1] == "blue":
                        if int(kugel[0]) > blue_load:
                            impossible = True
                            break
            if not impossible:
                total += index

            index += 1


    print("Total: {}".format(total))


if __name__ == "__main__":
    main()
