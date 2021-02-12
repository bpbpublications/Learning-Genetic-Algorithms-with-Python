import copy

import matplotlib.pyplot as plt
import os


def get_test_data():
    return [
        [56, 15], [77, 30], [12, 45], [35, 60], [30, 75], [0, 12], [55, 50]
    ]


def get_us_capitals():
    """
    https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
    ATT48 is a set of 48 cities (US state capitals) from TSPLIB. The minimal tour has length 33523.
    """
    points = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/att48_xy.txt') as fp:
        for cnt, line in enumerate(fp):
            x, y = line.strip().split(" ")[0], line.strip().split(" ")[-1]
            points.append([int(x), int(y)])
    return points


def distance(points, route):
    route_ext = copy.deepcopy(route)
    route_ext.append(route_ext[0])
    dist = 0
    for i in range(1, len(route_ext)):
        x_p = points[route_ext[i - 1]][0]
        x_c = points[route_ext[i]][0]
        y_p = points[route_ext[i - 1]][1]
        y_c = points[route_ext[i]][1]
        dist += pow((x_c - x_p)**2 + (y_c - y_p)**2, .5)
    return round(dist, 2)


def plot_route(points, route):
    route_ext = copy.deepcopy(route)
    route_ext.append(route_ext[0])
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    fig, ax = plt.subplots()
    ax.scatter(x, y, color = 'black')
    x_route = [x[r] for r in route_ext]
    y_route = [y[r] for r in route_ext]
    plt.plot(x_route, y_route, linestyle = '-', color = 'blue')

    plt.xticks([])
    plt.yticks([])
    plt.title(f"US State Capitals Problem \n"
              f"Distance: {distance(points, route)}")
    plt.show()
