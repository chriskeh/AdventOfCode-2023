#!/usr/bin/env /usr/bin/python


def main():

    test_flag = False
    time = []
    distance = []
    if test_flag:
        time.append(7)
        time.append(15)
        time.append(30)

        distance.append(9)
        distance.append(40)
        distance.append(200)
    else:
        time.append(60)
        time.append(80)
        time.append(86)
        time.append(76)

        distance.append(601)
        distance.append(1163)
        distance.append(1559)
        distance.append(1300)

    sum = 1
    for index, zeit in enumerate(time):
        counter = 0

        for speed in range(1,zeit):
            rest = zeit - speed
            wieweit = speed * rest
            if wieweit > distance[index]:
                counter += 1
            # print("{}, {}: {}".format(speed, rest, wieweit))

        sum *= counter

    print("Summe: {}".format(sum))

if __name__ == "__main__":
    main()
