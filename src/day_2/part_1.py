from __future__ import annotations
from typing import List, Tuple
import csv
from dataclasses import dataclass


@dataclass
class Level:
    reports: List[int]
    safety_low: List[int]
    safety_high: List[int]

    @classmethod
    def from_list(cls, row) -> List[Level]:
        reports = [int(v) for v in row]
        return Level(reports, 1, 4)

    def get_safety(self) -> bool:
        left_shift = self.reports[1:]
        diffs = [v1 - v for v, v1 in zip(left_shift, self.reports)]

        safe_values_pos = range(self.safety_low, self.safety_high)
        safe_values_neg = range(-self.safety_high+1, -self.safety_low+1)
        return all(diffs in safe_values_pos for diffs in diffs) | all(diff in safe_values_neg for diff in diffs)



if __name__ == '__main__':
    data_loc = "./day_2.txt"
    with open(data_loc, encoding="UTF-8", mode='r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        safe_count = 0
        total = 0
        for row in csv_reader:
            level = Level.from_list(row)
            safe_count += level.get_safety()
            total += 1

    print(safe_count)