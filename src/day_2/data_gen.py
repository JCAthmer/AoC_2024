import csv
import random
from src.day_2.part_1 import Level
from typing import List

def get_levels():
    data_loc = "./day_2.txt"
    with open(data_loc, encoding="UTF-8", mode='r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        safe = list()
        levels = list()

        for row in csv_reader:
            levels.append(Level.from_list(row))
    return levels

levels = get_levels()
# hundred_k = [random.choice(levels) for i in range(100000)]
# hundred_k_passing = sum(level.get_safety() for level in hundred_k)
#
# with open('100k_data.txt', 'w', encoding='UTF-8', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerows(level.reports for level in hundred_k)
#     print('100k', hundred_k_passing)
#
# ten_mill = [random.choice(levels) for i in range(10000000)]
# ten_mill_passing = sum(level.get_safety() for level in ten_mill)
#
# with open('10M_data.txt', 'w', encoding='UTF-8', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     for i, row in enumerate([level.reports for level in ten_mill]):
#         writer.writerow(row)
#         print(i)
#     print('10M', ten_mill_passing)

ten_mill = [random.choice(levels) for i in range(1000000)]
one_mill_passing = sum(level.get_safety() for level in ten_mill)

with open('1M_data.txt', 'w', encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for i, row in enumerate([level.reports for level in ten_mill]):
        writer.writerow(row)
        print(i)
    print('1M', one_mill_passing)
