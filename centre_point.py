from math import floor


def closer_point(x1, y1, x2, y2):
    x_1 = abs(x1)
    y_1 = abs(y1)
    x_2 = abs(x2)
    y_2 = abs(y2)
    first_point_coordinates_distance = x_1 + y_1
    second_point_coordinates_distance = x_2 + y_2
    if first_point_coordinates_distance <= second_point_coordinates_distance:
        return floor(x1), floor(y1)
    else:
        return floor(x2), floor(y2)


print(closer_point(float(input()), float(input()), float(input()), float(input())))
