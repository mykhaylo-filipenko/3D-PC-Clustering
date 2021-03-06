import os
import shutil
import sys
from os import path
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN, KMeans, Birch, OPTICS, MeanShift, AgglomerativeClustering, SpectralClustering




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
                print("line = ", line)
                line[0] = (str(float(line[0]) + (i + 2)))
                line[1] = (str(float(line[1]) + 8 * (i + 2)))
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
                print("line = ", line)
                line[0] = (str(float(line[0]) + (i + 2)))
                line[1] = (str(float(line[1]) + 2 * (i - 1)))
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
        if not path.exists(sys.argv[2]):
            os.mkdir("ProcessedData")
        else:
            shutil.rmtree(sys.argv[2])
            os.mkdir("ProcessedData")
        i = 0
        directories = sys.argv[3]
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
        directories = sys.argv[3]
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
