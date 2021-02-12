import numpy as np

from ch8.functions import complicated_one

maximum = 0
counter = 0

for a in np.arange(0., 1., .02):
    for b in np.arange(0, 1, .02):
        for x in np.arange(-100, 101, .2):
            for n in range(0, 21):
                for fun_name in ['cos', 'sin']:
                    counter += 1
                    val = complicated_one(a, b, x, n, fun_name)
                    if val > maximum:
                        maximum = val

print(f'Brute force maximum: {maximum} , counter: {counter}')
