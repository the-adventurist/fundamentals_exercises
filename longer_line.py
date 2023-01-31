from math import floor


def longer_line(start_first_line_x, start_first_line_y, final_first_line_x, final_first_line_y,
                start_second_line_x, start_second_line_y, final_second_line_x, final_second_line_y):
    x1_s = abs(x1)
    y1_s = abs(y1)
    x1_f = abs(x2)
    y1_f = abs(y2)
    x2_s = abs(x1)
    y2_s = abs(x1)
    x2_f = abs(x1)
    y2_f = abs(x1)
    first_point_coordinates_distance = x_1 + y_1
    second_point_coordinates_distance = x_2 + y_2
    if first_point_coordinates_distance <= second_point_coordinates_distance:
        return floor(x1), floor(y1)
    else:
        return floor(x2), floor(y2)


print(closer_point(float(input()), float(input()), float(input()), float(input())))
