import os
import shutil
import sys


# This method  will be never used after the data processing
def processor(file):
    with open(file, 'r+') as file:
        arr = []
        while True:
            line = file.readline()
            if not line:
                break
            arr.append(line.replace(' ', ', ').replace('\n', ',\n'))
        file.truncate(0)
        matrix = [x.split() for x in arr]
        print([x.split() for x in arr])
        for arr in matrix:
            for ind in range(len(arr)):
                if ind == len(arr) - 1:
                    file.write(arr[ind] + "\n")
                else:
                    file.write(arr[ind] + " ")


def move(file):
    shutil.move(file, sys.argv[2])  # sys.argv[2] - directory, where to move the data


def main():
    directories = sys.argv[1]  # sys.argv[1] - directory, where to find the data
    for subdir, dirs, files in os.walk(directories):
        for file in files:
            processor(os.path.join(subdir, file))
            move(os.path.join(subdir, file))


if __name__ == '__main__':
    main()
