from collections.abc import Iterable

with open('input', 'r') as file1:
    readings = [int(v) for v in file1.read().splitlines() if len(v) > 0]

def sliding_window(seq: Iterable, window: int):
    return [seq[i: i + window] for i in range(len(seq) - window + 1)]

readings_windows = sliding_window(readings, 3)

readings_windows_sums = [sum(v) for v in readings_windows]


readings_tuples = sliding_window(readings_windows_sums, 2)

increased_readings = [v for v in readings_tuples if v[0] < v[1]]

for v in increased_readings:
    print(v)

print(len(increased_readings))
