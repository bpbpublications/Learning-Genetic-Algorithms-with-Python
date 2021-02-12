import math
from math import nan


def average(series, period):
    if len(series) < period + 1:
        return nan
    else:
        return sum(series[-period - 1:-1]) / period


def is_improvement_positive(population_fit, period = 10, gap = .01):
    avg = average(population_fit, period)
    if math.isnan(avg) or avg == 0:
        return True
    return population_fit[-1] > avg * (1 - gap)
