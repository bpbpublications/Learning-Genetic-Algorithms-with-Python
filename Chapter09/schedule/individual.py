import random
from math import floor

import pandas as pd
import matplotlib.pyplot as plt


class Individual:
    counter = 0
    period = 0
    employees = 0

    @classmethod
    def set_fitness_function(cls, fun):
        cls.fitness_function = fun

    @classmethod
    def set_period(cls, period):
        cls.period = period

    @classmethod
    def set_employees(cls, employees):
        cls.employees = employees

    @classmethod
    def generate_random(cls):
        return Individual([random.choice([0, 1]) for _ in range(cls.period * cls.employees * 3)])

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = self.__class__.fitness_function(self.create_schedule())
        self.__class__.counter += 1

    def create_schedule(self):
        t = {}
        for e in range(1, self.employees + 1):
            shift_len = 3 * self.period
            t[e] = self.gene_list[shift_len * (e - 1): shift_len * e]
        schedule_df = pd.DataFrame(data = t)
        return schedule_df

    def plot_schedule(self):
        schedule_df = self.create_schedule()
        x_labels = []
        shift_names = {0: 'mor', 1: 'mid', 2: 'evn'}
        for i in range(0, 3 * self.period):
            day = floor(i / 3) + 1
            shift = shift_names[i % 3]
            x_labels.append(f'Day {day} : {shift}')
        plt.xticks(list(range(0, 3 * self.period)), x_labels, rotation = 90)
        y_labels = []
        for i in range(0, self.employees):
            y_labels.append(f'Emp: {i+1}')
        plt.yticks(list(range(0, self.employees)), y_labels)
        plt.imshow(schedule_df.T, cmap = 'binary')
        plt.title(f'Fitness: {self.fitness}')
        plt.show()
        plt.close()


if __name__ == '__main__':

    random.seed(9)

    Individual.set_employees(5)
    Individual.set_period(7)


    def fitness_function(df):
        return 0


    Individual.set_fitness_function(fitness_function)

    ind = Individual.generate_random()
    ind.plot_schedule()
