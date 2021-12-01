with open('input', 'r') as file1:
    readings = [int(v) for v in file1.read().splitlines() if len(v) > 0]

readings_tuples = [(readings[ind-1],value) for ind, value in enumerate(readings)]

increased_readings = [v for v in readings_tuples if v[0] < v[1]]

for v in increased_readings:
    print(v)

print(len(increased_readings))
