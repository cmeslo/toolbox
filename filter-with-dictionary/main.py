
def build_dictionary(path):
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.strip().split(',')
            d[key] = val
    return d


def handle_file(d, path):
    with open('./new1.txt', 'w') as new_file1, open('./new2.txt', 'w') as new_file2:
        with open(path) as old_file:
            for line in old_file:
                key = line[96:113]
                if key in d:
                    new_line = line[0:96] + d[key] + line[113:]
                    new_file1.write(new_line)
                else:
                    new_file2.write(line)


def main():
    d = build_dictionary('./dict.txt')
    handle_file(d, './ABCS_REPORT_FILE_20180601.TXT')


if __name__ == "__main__":
    main()
