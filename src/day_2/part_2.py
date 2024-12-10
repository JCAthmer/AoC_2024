from __future__ import annotations
from typing import List, Tuple
import csv
from dataclasses import dataclass


@dataclass
class Level:
    reports: List[int]
    pos_safety: range[int, int]
    neg_safety: range[int, int]

    @classmethod
    def from_list(cls, row, safe_values_neg, safe_values_pos) -> List[Level]:
        reports = [int(v) for v in row]
        return Level(reports, safe_values_neg, safe_values_pos)

    @staticmethod
    def calc_diffs(reports: List[int]) -> List[int]:
        left_shift = reports[1:]
        diffs = [v1 - v for v, v1 in zip(left_shift, reports)]
        return diffs

    def get_safe_bools(self, diffs: List[int]) -> Tuple[List[bool], List[bool]]:
        safe_positive = [diffs in self.pos_safety for diffs in diffs]
        safe_negative = [diffs in self.neg_safety for diffs in diffs]
        return safe_positive, safe_negative

    def get_safety(self) -> bool:
        diffs = self.calc_diffs(self.reports)
        safe_bools_pos, safe_bools_neg = self.get_safe_bools(diffs)

        safe = all(safe_bools_pos) | all(safe_bools_neg)
        if safe:
            return safe
        elif sum(1 for v in safe_bools_pos if v is False) < 3:
            return self.dampener(self.reports, safe_bools_pos)
        elif sum(1 for v in safe_bools_neg if v is False) < 3:
            return self.dampener(self.reports, safe_bools_neg)
        else:
            return safe

    def dampener(self, reports: List[int], safe_bools) -> bool:
        failed_diff = next(i for i, bool in enumerate(safe_bools) if not bool)
        dampened_left = reports.copy()
        dampened_right = reports.copy()
        del dampened_left[failed_diff]
        del dampened_right[failed_diff+1]
        dampened_diffs_l = self.calc_diffs(dampened_left)
        dampened_diffs_r = self.calc_diffs(dampened_right)

        safe_bools_pos_l, safe_bools_neg_l = self.get_safe_bools(dampened_diffs_l)
        safe_bools_pos_r, safe_bools_neg_r = self.get_safe_bools(dampened_diffs_r)

        return all(safe_bools_pos_l) | all(safe_bools_neg_l) | all(safe_bools_pos_r) | all(safe_bools_neg_r)



if __name__ == '__main__':
    data_loc = "./10M_data.txt"
    safe_values_pos = range(1, 4)
    safe_values_neg = range(-3, 0)
    with open(data_loc, encoding="UTF-8", mode='r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        safe_count = 0
        total = 0
        for i, row in enumerate(csv_reader):
            level = Level.from_list(row, safe_values_pos, safe_values_neg)
            total += 1
            safe_count += level.get_safety()

    print(safe_count)