import csv
import math

import numpy as np
import os

target_data = [[] for i in range(18)]
X_train = []
Y_train = []


def read_csv() -> None:
    with open('../data1/train.csv', 'r', encoding='gb18030') as target_csv:
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
    read_csv()
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
    # iteration = 100
    # weights = np.ones(18 * 9)
    # learning_rate = 0.01
    # gra_2_sum = np.ones(18 * 9)
    # for i in range(iteration):
    #     gradient = np.zeros(18 * 9)
    #     variance = 0
    #     for j in range(len(X_train)):
    #         loss = np.dot(weights, X_train[j]) - Y_train[j]
    #         variance += loss ** 2
    #         gradient = 2 * np.dot(X_train[j].T, loss)
    #         gra_2_sum += gradient ** 2
    #         ada = np.sqrt(gra_2_sum + 1e-8)
    #         weights -= learning_rate * gradient / ada
    #     if i % 10 == 0:
    #         cost = variance / len(X_train)
    #         cost_a = math.sqrt(cost)
    #         print(i, " times ", " variance: ", cost, " standard deviation: ", cost_a)
    # np.save('model.npy', 'w')
    w = np.load('model.npy')
    text = open('../data1/test.csv', 'r')
    row = csv.reader(text, delimiter=',')
    pre_list = []
    for i in range(len(X_train)):
        pre_result = np.dot(weights, X_test[i])
        pre_list.append(pre_result)


