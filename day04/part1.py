#!/usr/bin/env /usr/bin/python

def main():

    input_data_file = "part1.data"
    sum = 0

    with open(input_data_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            fields = line.split(':')
            numbers = fields[1].split('|')
            lucky_numbers = numbers[0].split()
            my_numbers = numbers[1].split()

            # convert to a set and use the intersection method of sets
            result = set(lucky_numbers).intersection(my_numbers)
            hits = len(result)
            if hits > 0:
                line_sum = 2 ** (hits -1)
                sum += line_sum

        print("Total: {}".format(sum))

if __name__ == "__main__":
    main()
