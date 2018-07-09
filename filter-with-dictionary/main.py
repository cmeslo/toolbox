
def build_dictionary(path):
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.strip().split(',')
            d[key] = val
    return d


def handle_file(d, path):
    with open('./result1.txt', 'w') as new_file1, open('./result2.txt', 'w') as new_file2:
        with open(path) as old_file:
            for line in old_file:
                key = line[7:11]
                if key in d:
                    new_line = line[0:7] + d[key] + line[11:]
                    new_file1.write(new_line)
                else:
                    new_file2.write(line)


def main():
    d = build_dictionary('./dict.txt')
    handle_file(d, './test.txt')


if __name__ == "__main__":
    main()
