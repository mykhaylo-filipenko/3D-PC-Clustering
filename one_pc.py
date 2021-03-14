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
                #line = [str(float(elem) + 3 * i) for elem in line]
                line = [str(float(elem)) for elem in line]
                line[1] = (str(float(line[1]) + 5 * (i + 1)))
                # line[len(line) - 1] = str((float(line[len(line) - 1]) - i))
                for elem in line:
                    elem += ','
                print("line = ", line)
                result.append(line)
    return result


def processor_tree(file, i):
    result = []
    print("Converting the data...")
    with open(file, 'r+') as file:
        while file.readline():
            line = file.readline()
            if line:
                line = line.split()
                line = [str(float(elem) + 3 * i) for elem in line]
                line[1] = (str(float(line[1]) + 2 * (i - 3)))
                # line[len(line) - 1] = str((float(line[len(line) - 1]) - i))
                for elem in line:
                    elem += ','
                print("line = ", line)
                result.append(line)
    return result


def move(matrix):
    print("Moving file to correct directory...")

    file = open("output.txt", "w")
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
        if not path.exists("D:/NULP/diploma/3D-PC-Clustering/ProcessedData/"):
            os.mkdir("ProcessedData")
        else:
            shutil.rmtree("D:/NULP/diploma/3D-PC-Clustering/ProcessedData/")
            os.mkdir("ProcessedData")
        i = 0
        directories = "D:/NULP/diploma/urban_scenes_sketchup/urban_scenes_sketchup/car24/"
        for subdir, dirs, files in os.walk(r'{}'.format(directories)):
            for file in files:
                print(file)
                if i < 4:
                    res = processor(os.path.join(subdir, file), i)
                    for elem in res:
                        matrix.append(elem)
                    move(matrix)
                    i += 1
            print(matrix)
        i = 0
        directories = "D:/NULP/diploma/urban_scenes_sketchup/urban_scenes_sketchup/3d_tree20/"
        for subdir, dirs, files in os.walk(r'{}'.format(directories)):
            for file in files:
                print(file)
                if i < 2:
                    res = processor_tree(os.path.join(subdir, file), i)
                    for elem in res:
                        matrix.append(elem)
                    move(matrix)
                    i += 1
            move(matrix)


if __name__ == '__main__':
    main()
