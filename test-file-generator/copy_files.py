import os
import errno
import shutil


def makefiles(content):
    # print(*content, sep='\n')
    for i, c in enumerate(content):
        filename = os.path.dirname(__file__) + '/test' + c
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        shutil.copyfile('./test.txt', filename)
        print('file ' + str(i) + ': ' + c + ' copied')


def main():
    with open('./files.txt') as f:
        content = [x.strip() for x in f.readlines()]
        content = [s.replace('YYYYMMDD', '20180628') for s in content]
        content = [s.replace('YYMMDD', '180628') for s in content]

    makefiles(content)


if __name__ == "__main__":
    main()
