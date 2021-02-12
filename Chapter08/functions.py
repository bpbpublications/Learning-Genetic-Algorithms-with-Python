import math


def complicated_one(a, b, x, n, fun_name):
    sum_ = 0
    for i in range(10, 10 + n + 1):
        if fun_name == 'cos':
            trig_value = math.cos(math.log2(b**n + 1) * math.pi * x) /\
                         (n + 1) + math.sin(x)**n
        elif fun_name == 'sin':
            trig_value = math.sin(math.log2(b**n + 1) * math.pi * x) /\
                         (n + 1) + math.cos(x)**n
        else:
            raise Exception(f'Unknown Function: {fun_name}')
        resid = trig_value - math.log2(n + 1)
        div = ((n + 1)**2) * (1 + a + b) * (120 - x**2) * resid + 1 / 2
        sum_ += ((x * n + math.log(n + 1)) / div) / (10**15)
    return sum_
