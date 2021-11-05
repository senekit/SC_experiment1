import csv

import numpy as np
import os

target_data = [[] for i in range(18)]
X_train = []
Y_train = []


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


# def handle_data() -> None:
#     for month in range(12):
#         for group in range(471):
#             X_train.append([])
#             for attribute in range(18):
#                 for hour in range(9):
#                     X_train[month*471 + group].append(target_data[attribute][month * 480 + group + hour])
#             Y_train.append(target_data[9][month * 480 + group + 9])
#     X_train = np.array(X_train)
#     Y_train = np.array(Y_train)
#

if __name__ == '__main__':
    file_path = '../data1/train.csv'
    read_csv(file_path=file_path)
    print(np.array(target_data).shape)
    X_train = []
    Y_train = []
    for month in range(12):
        for group in range(471):
            X_train.append([])
            for attribute in range(18):
                for hour in range(9):
                    X_train[month * 471 + group].append(target_data[attribute][month * 480 + group + hour])
            Y_train.append(target_data[9][month * 480 + group + 9])
    X_train = np.array(X_train)
    Y_train = np.array(Y_train)
    print(np.array(X_train).shape)