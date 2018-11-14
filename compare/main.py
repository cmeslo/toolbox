def build_list(path):
    array = []
    with open(path) as f:
        for line in f:
            # (num, mnt) = line.strip().split(',')
            # array.append((num, mnt))
            array.append(line.strip())
    return array


def compare(list1, list2):
    with open('./data/same.txt', 'w') as same:
        for item in list(list2):
            if item in list(list1):
                list1.remove(item)
                list2.remove(item)
                # same.write(''.join('{},{}'.format(item[0], item[1])) + '\n')
                same.write(item + '\n')

    with open('./data/diff1.txt', 'w') as diff1:
        for item in list1:
            # diff1.write(''.join('{},{}'.format(item[0], item[1])) + '\n')
            diff1.write(item + '\n')

    with open('./data/diff2.txt', 'w') as diff2:
        for item in list2:
            # diff2.write(''.join('{},{}'.format(item[0], item[1])) + '\n')
            diff2.write(item + '\n')


def main():
    list1 = build_list('./data/1.txt')
    list2 = build_list('./data/2.txt')
    compare(list1, list2)


if __name__ == "__main__":
    main()
