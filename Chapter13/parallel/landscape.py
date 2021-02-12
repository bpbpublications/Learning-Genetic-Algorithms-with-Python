import copy
import random
from enum import Enum, auto

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, cm
import matplotlib.patches as mpatches

from ch13.parallel.individual import Individual


class SquareType(Enum):
    water = auto()
    land = auto()
    hill = auto()
    city = auto()


class Square:

    def __init__(self, type, needs_coverage, tower_cost, is_covered = False):
        self.type = type
        self.needs_coverage = needs_coverage
        self.is_covered = is_covered
        self.tower_cost = tower_cost
        self.has_radar = False

    def __repr__(self) -> str:
        return self.type.name()


class Landscape:

    def __init__(self, matrix):
        self.matrix = matrix

    def rows(self):
        return len(self.matrix)

    def cols(self):
        return len(self.matrix[0])

    def add_radars(self, coordinates, radius):
        for i in range(self.rows()):
            for j in range(self.cols()):
                if coordinates[i][j] == 1:
                    self.matrix[i][j].has_radar = True
                    for i1 in range(self.rows()):
                        for j1 in range(self.cols()):
                            if (i1 - i)**2 + (j1 - j)**2 <= radius**2:
                                self.matrix[i1][j1].is_covered = True

    def uncovered_count(self):
        count = 0
        for i in range(self.rows()):
            for j in range(self.cols()):
                sqr = self.matrix[i][j]
                if sqr.needs_coverage and not sqr.is_covered:
                    count += 1
        return count

    def radar_cost(self):
        cost = 0
        for i in range(self.rows()):
            for j in range(self.cols()):
                if self.matrix[i][j].has_radar:
                    cost += self.matrix[i][j].tower_cost
        return cost


def plot_landscape(landscape):
    square_colors = {
        SquareType.water: 1,
        SquareType.land:  11,
        SquareType.hill:  21,
        SquareType.city:  31
    }
    m = np.empty([landscape.rows(), landscape.cols()])
    for i in range(landscape.rows()):
        for j in range(landscape.cols()):
            m[i, j] = square_colors[landscape.matrix[i][j].type]
    col_list = ['blue', 'green', 'brown', 'black']
    labels = [s.name for s in square_colors.keys()]
    cmap = colors.ListedColormap(col_list)
    bounds = [0, 10, 20, 30, 40]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(m, cmap = cmap, norm = norm)
    plt.grid(which = 'major', axis = 'both', linestyle = '--', color = 'k', linewidth = 1)
    patches = [mpatches.Patch(color = col_list[i], label = labels[i]) for i in range(len(col_list))]
    plt.legend(handles = patches, loc = 4, borderaxespad = 0.)
    plt.title('Landscape')
    plt.show()


def plot_coverage(landscape, title = "Coverage"):
    coverage_colors = {
        'neutral':        1,
        'is covered':     11,
        'needs coverage': 21
    }

    m = np.empty([landscape.rows(), landscape.cols()])
    for i in range(landscape.rows()):
        for j in range(landscape.cols()):
            if landscape.matrix[i][j].is_covered:
                m[i, j] = coverage_colors['is covered']
            elif not landscape.matrix[i][j].needs_coverage:
                m[i, j] = coverage_colors['neutral']
            elif landscape.matrix[i][j].needs_coverage:
                m[i, j] = coverage_colors['needs coverage']

    col_list = ['white', 'green', 'red']
    labels = list(coverage_colors.keys())
    cmap = colors.ListedColormap(col_list)
    bounds = [0, 10, 20, 30]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(m, cmap = cmap, norm = norm)
    plt.grid(which = 'major', axis = 'both', linestyle = '--', color = 'k', linewidth = 1)
    patches = [mpatches.Patch(color = col_list[i], label = labels[i]) for i in range(len(col_list))]
    plt.legend(handles = patches, loc = 4, borderaxespad = 0.)
    plt.title(title)
    plt.show()


def plot_costs(landscape):
    m = np.empty([landscape.rows(), landscape.cols()])
    for i in range(landscape.rows()):
        for j in range(landscape.cols()):
            m[i, j] = landscape.matrix[i][j].tower_cost
    plt.imshow(m, cmap = cm.Reds)
    plt.colorbar()
    plt.title('Radar Construction Costs')
    plt.show()


def generate_random_landscape(points, weights, rows, cols):
    matrix = [[None] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            p = random.choices(points, weights.values())
            square = copy.deepcopy(p[0])
            square.tower_cost = round(square.tower_cost * (1 + random.uniform(0, .1)))
            matrix[i][j] = square
    return Landscape(matrix)
