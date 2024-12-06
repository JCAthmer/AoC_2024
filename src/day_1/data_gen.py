from typing import Tuple, List
import csv
import random



def gen_data(data_loc, data_size) -> Tuple[List[int], List[int]]:
    group_1 = list()
    group_2 = list()

    with open(data_loc, encoding="UTF-8", mode='r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        for row in csv_reader:
            group_1.append(int(row[0]))
            group_2.append(int(row[3]))

    max_value = max(group_1+group_2)
    min_value = min(group_1+group_2)

    return [random.randint(min_value, max_value) for i in range(data_size)], [random.randint(min_value, max_value) for i in range(data_size)]

data_loc = "./day_1.txt"

hundred_k_l, hundred_k_r  = gen_data(data_loc, 100000)
ten_mill_l, ten_mill_r = gen_data(data_loc, 10000000)

with open("./day_1_100k.txt", "w", encoding="UTF-8", newline='') as file:
    csv_writer = csv.writer(file, delimiter=' ')
    for l, r in zip(hundred_k_l, hundred_k_r):
        csv_writer.writerow([l,"","",r])

with open("./day_1_10M.txt", "w", encoding="UTF-8", newline='') as file:
    csv_writer = csv.writer(file, delimiter=' ')
    for l, r in zip(ten_mill_l, ten_mill_r):
        csv_writer.writerow([l, "", "", r])