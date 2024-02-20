import sys


def location_of_the_point(file_point_radius, file_point):
    point_xc, point_yc, radius = read_first_file(file_point_radius)
    points = read_second_file(file_point)

    for i in points:
        points = i.split()
        point_x = float(points[0])
        point_y = float(points[1])
        val = (point_x - point_xc) ** 2 + (point_y - point_yc) ** 2 - radius ** 2
        if val < 0:
            print(f'{point_x}, {point_y} - 1')
        elif val > 0:
            print(f'{point_x}, {point_y} - 2')
        else:
            print(f'{point_x}, {point_y} - 3')


def read_first_file(file_name):
    with open(file_name, 'r') as file:
        points = file.readline()
        points_list = points.split()
        point_xc = float(points_list[0])
        point_yc = float(points_list[1])
        radius = float(file.readline())
    return point_xc, point_yc, radius


def read_second_file(file_name):
    with open(file_name, 'r') as file:
        point_list = file.read().split("\n")
    return point_list


argument_list = sys.argv[1:]
first_file = argument_list[0]
second_file = argument_list[1]


location_of_the_point(first_file, second_file)
