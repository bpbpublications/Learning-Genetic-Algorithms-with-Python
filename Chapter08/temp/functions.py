import math


def dummy_function(x):
    even_sum = 0
    even_count = 0
    prod = 1
    for d in str(x):
        digit = int(d)
        prod *= digit
        if digit % 2 == 0:
            even_sum += digit
            even_count += 1
    return math.factorial(even_sum) * x / prod**even_count


def enum_function(fun_name, x, n):
    if fun_name == 'cos':
        return math.cos(x)**n
    elif fun_name == 'sin':
        return math.sin(x)**n
    elif fun_name == 'log':
        return math.log(x, 2)**n
    elif fun_name == 'exp':
        return math.exp(x)**n
    else:
        raise Exception(f'Unknown Function: {fun_name}')


def weierstrass(a, b, x, n, fun_name):
    sum_ = 0
    for i in range(0, n + 1):
        if fun_name == 'cos':
            trig_value = math.cos((b**n) * math.pi * x)
        elif fun_name == 'sin':
            trig_value = math.sin((b**n) * math.pi * x)
        else:
            raise Exception(f'Unknown Function: {fun_name}')
        sum_ += a**n * trig_value

    return sum_


def some_function(op_major, op_minor, v1, v2):
    sign = math.copysign(1, op_minor)
    if op_major == 0:
        return v1 + abs(v2 - 15) - 100 * sign
    elif op_major == 1:
        return v1 * abs(v2 - 15) - 100 * sign
    elif op_major == 2:
        return pow(v1 + abs(v2 - 15), 3) - 100 * sign
    elif op_major == 3:
        return pow(v1 + abs(v2 - 15), 2) - 100 * sign
    elif op_major == 4:
        return 0,
    elif op_major == 5:
        return pow(v1 + abs(v2 - 15), 3) + 100 * sign


if __name__ == '__main__':

    print(some_function(1, 3, 8, 0))
