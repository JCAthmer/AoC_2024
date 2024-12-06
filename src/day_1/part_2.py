import csv
from typing import Tuple, List

data_loc = "./day_1_10M.txt"

def get_data(data_loc) -> Tuple[List[int], List[int]]:
    group_1 = list()
    group_2 = list()

    with open(data_loc, encoding="UTF-8", mode='r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        for row in csv_reader:
            group_1.append(int(row[0]))
            group_2.append(int(row[3]))

    return group_1, group_2

def standard(group_1: List[int], group_2: List[int]) -> float:
    sim_scores = list()
    for g1 in group_1:
        sim_scores.append(g1*sum(1 for v in group_2 if g1 == v))

    return sum(sim_scores)

def map_method(group_1: List[int], group_2: List[int]) -> float:
    offset = min(group_1+group_2)
    max_v = max(group_1+group_2)
    g1_map = [0] * (max_v - offset + 1)
    g2_map = [0] * (max_v - offset + 1)
    for g1, g2 in zip(group_1, group_2):
        g1_map[g1-offset] += 1
        g2_map[g2-offset] += 1
    a = 0
    return sum((i+offset)*c1*c2 for i, (c1, c2) in enumerate(zip(g1_map, g2_map)))




if __name__ == "__main__":
    group_1, group_2 = get_data(data_loc)
    print(map_method(group_1, group_2))
    # print(standard(group_1, group_2))
