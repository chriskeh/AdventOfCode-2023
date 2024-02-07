#!/usr/bin/env /usr/bin/python

def main():

    input_data_file = ("part1.data")
    amount = []

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
            if hits == 0:
                amount.append(0)
            else:
                amount.append(hits)

        print("Amount: {}".format(amount))
        result = [1] * len(amount)

        zeile = 0
        for current_hits in amount:
            if current_hits > 0:
                index = 1
                # print("\nZeile {}: Hits {}".format(zeile, current_hits))
                while index <= current_hits:
                    position = zeile + index
                    if position <= len(numbers) + 2:
                        result[position] += result[zeile]
                        index += 1
                    else:
                        index = current_hits + 1
                # print("In Loop: {}".format(result))
            zeile += 1

        total = 0
        for number in result:
            total += number
        print("Total: {} ({})".format(total, result))

if __name__ == "__main__":
    main()
