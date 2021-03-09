import os
import shutil
import sys
from os import path


# This method  will be never used after the data processing
def processor(file, i):
    result = []
    print("Converting the data...")
    with open(file, 'r+') as file:
        while file.readline():
            line = file.readline()
            if line:
                line = line.split()
                line = [str(float(elem) + i) for elem in line]
                for elem in line:
                    elem += ','
                print("line = ", line)
                result.append(line)
    return result


def move(matrix):
    print("Moving file to correct directory...")

    file = open("output.txt", "a")
    print(len(matrix))
    for arr in matrix:
        for ind in range(len(arr)):
            if ind == len(arr) - 1:
                file.write(arr[ind] + "\n")
            else:
                file.write(arr[ind] + " ")


def main():
    matrix = []
    if sys.argv[1] == '1':
        if not path.exists(sys.argv[3]):
            os.mkdir("ProcessedData")
        else:
            shutil.rmtree(sys.argv[3])
            os.mkdir("ProcessedData")
        i = 0
        directories = sys.argv[2]
        for subdir, dirs, files in os.walk(r'{}'.format(directories)):
            for file in files:
                if i < 5:
                    res = processor(os.path.join(subdir, file), i)
                    for elem in res:
                        matrix.append(elem)
                    move(matrix)
                    i += 1
            move(matrix)


if __name__ == '__main__':
    main()
