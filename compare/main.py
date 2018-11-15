def build_list(path):
    with open(path) as f:
        return [line.strip() for line in f]


def compare(list1, list2):
    with open('./data/same.txt', 'w') as same:
        for item in list(list2):
            if item in list1:
                list1.remove(item)
                list2.remove(item)
                same.write(item + '\n')

    with open('./data/diff1.txt', 'w') as diff1, open('./data/diff2.txt', 'w') as diff2:
        diff1.write('\n'.join([item for item in list1]))
        diff2.write('\n'.join([item for item in list2]))


def main():
    list1 = build_list('./data/1.txt')
    list2 = build_list('./data/2.txt')
    compare(list1, list2)


if __name__ == "__main__":
    main()
