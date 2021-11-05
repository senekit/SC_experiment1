import csv

import numpy as np
import os

target_data = [[] for i in range(18)]


def read_csv(file_path: str) -> None:
    with open(file_path, 'r') as target_csv:
        target_reader = csv.reader(target_csv)
        target_reader.__next__()
        count = 0
        for row in target_reader:
            for i in range(3, 27):
                if row[i] == "NR":
                    target_data[count % 18].append(float(0))
                else:
                    target_data[count % 18].append(float(row[i]))
            count += 1


if __name__ == '__main__':
    file_path = '../data1/train.csv'
    read_csv(file_path=file_path)
    print(np.array(target_data).shape)