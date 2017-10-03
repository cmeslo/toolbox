import collections


def main():
    with open('./files.txt') as f:
        counts = collections.Counter(l.strip() for l in f)

    for line, count in counts.most_common():
        print(count, line)


if __name__ == "__main__":
    main()
