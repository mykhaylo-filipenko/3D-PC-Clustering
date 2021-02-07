import os
import shutil
import sys


# This method  will be never used after the data processing
def processor(file):
    print("Converting the data...")
    with open(file, 'r+') as file:
        arr = []
        while True:
            line = file.readline()
            if not line:
                break
            arr.append(line.replace(' ', ', ').replace('\n', ',\n'))
        file.truncate(0)
        matrix = [x.split() for x in arr]

        for arr in matrix:
            for ind in range(len(arr)):
                if ind == len(arr) - 1:
                    file.write(arr[ind] + "\n")
                else:
                    file.write(arr[ind] + " ")


def move(file):
    print("Moving file to correct directory...")
    shutil.copy(file, sys.argv[3])


def main():
    if sys.argv[1] == '1':
        directories = sys.argv[2]
        for subdir, dirs, files in os.walk(r'{}'.format(directories)):
            for file in files:
                processor(os.path.join(subdir, file))
                move(os.path.join(subdir, file))


if __name__ == '__main__':
    main()
