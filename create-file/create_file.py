import sys


def create(file_name, row_len, col_len):
    with open(file_name, 'wb') as f:
        for r in range(row_len):
            row = b''
            for c in range(col_len):
                row += b'0'
            row += b'\r\n'
            f.write(row)

    f.close()

if __name__ == "__main__":
    # create('create_test.txt', 4, 1195)
    if len(sys.argv) == 4:
        create(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
        print('create file ' + sys.argv[1] + ' success.')
    else:
        print('parameter error!')
