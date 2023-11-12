from math import cos


def cos_wave():
    n = 10
    step_size = 0.1
    points = []
    x = 0
    while x < n:
        points.append([x, cos(x)])
        x += step_size

    print(points)
    return points


carbon_age_tbl = [
    [0.78, 2050],
    [0.8, 1850],
    [0.82, 1650],
    [0.84, 1450],
    [0.86, 1250],
    [0.88, 1050],
    [0.9, 870],
    [0.92, 690],
]
