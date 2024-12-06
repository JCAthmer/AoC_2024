from datetime import datetime
start = datetime.now()
import csv


data_loc = "./day_1.txt"

def standard(data_loc: str) -> int:
    group_1 = list()
    group_2 = list()

    with open(data_loc,encoding = "UTF-8", mode='r') as file:
        csv_reader = csv.reader(file , delimiter=' ')
        for row in csv_reader:
            group_1.append(int(row[0]))
            group_2.append(int(row[3]))

    group_1.sort()
    group_2.sort()

    diff = sum(abs(v1 -v2) for v1, v2 in zip(group_1, group_2))
    return diff

if __name__ == '__main__':
    print(standard(data_loc))
    end = datetime.now()
    print((end - start).microseconds)