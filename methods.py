import numpy as np
import pandas as pd

limit = 10000


def bisection_method(a, b, function, eps):
    a_ = []
    b_ = []
    x_ = []
    fa = []
    fb = []
    fx = []
    ab = []
    i = 1
    while True:
        x = (a + b) / 2
        x_.append(x)
        y = function(x)
        fx.append(y)
        if function(a) * y > 0:
            a = x
        else:
            b = x
        a_.append(a)
        b_.append(b)
        fa.append(function(a))
        fb.append(function(b))
        ab.append(abs(a - b))
        if abs(a - b) <= eps:
            break
        i += 1
        assert i < limit, f"Не удалось найти решение за {limit} итераций"
    log = pd.DataFrame({'a': a_, 'b': b_, 'x': x_, 'f(a)': fa, 'f(b)': fb, 'f(x)': fx, '|a - b|': ab}, index=[j+1 for j in range(i)])
    return i, x, log


def secants_method(a, b, f, eps):
    xp = []
    xn = []
    dif = []
    x_ = []
    row = []
    start = a
    if f(a) * Derivative(Derivative(f))(a) > 0:
        start = a
    elif f(b) * Derivative(Derivative(f))(b) > 0:
        start = b
    x = [start, start - 0.5 * ((b - a) / (-b + a))]
    i = 1
    while True:
        row.append(i)
        fp = f(x[i - 1])
        fx = f(x[i])
        x.append(x[i] - (x[i] - x[i - 1]) / (fx - fp) * fx)
        x_.append(x[i])
        xp.append(x[i - 1])
        xn.append(x[i + 1])
        dif.append(abs(x[i] - x[i + 1]))
        if abs(x[i] - x[i + 1]) <= eps or abs(fx) <= eps:
            break
        assert i < limit, f"Не удалось найти решение за {limit} итераций"
        i += 1
    fx = [f(i) for i in x_]
    fxp = [f(i) for i in xp]
    fxn = [f(i) for i in xn]
    log = pd.DataFrame(
        {'x(k-1)': xp, 'f(x(k-1))': fxp, 'xk': x_, 'f(xk)': fx, 'x(k+1)': xn, 'f(x(k+1))': fxn, '|xk - x(k+1)|': dif},
        index=row)
    return i, x[i + 1], log


def simple_iteration_method(a, b, f, eps):
    x = [a]
    xn = []
    dif = []
    row = []
    i = 0
    x_ = np.array([a + 0.1 * i for i in range((int(b - a)+1) * 10 + 1)])
    der = Derivative(f)
    y_ = np.array([der(x) for x in x_])
    lambda_ = 1 / -np.max(y_)
    new_coefs = [coef * lambda_ for coef in f.coefs]
    new_coefs[-2] += 1
    y = Function(new_coefs)
    print(np.max(y_))
    while True:
        row.append(i + 1)
        x.append(y(x[i]))
        xn.append(x[i + 1])
        dif.append(abs(x[i + 1] - x[i]))
        if abs(x[i + 1] - x[i]) <= eps:
            x = x[:-1]
            break
        assert i < limit, f"Не удалось найти решение за {limit} итераций"
        i += 1
    fx = [f(i) for i in x]
    log = pd.DataFrame({'xi': x, 'f(xi)': fx, 'x(i+1)': xn, 'phi(xi))': xn, '|x(i+1) - xi|': dif})
    return i, x[i], log


class Function:
    def __init__(self, coefs):
        self.power = len(coefs) - 1
        self.coefs = coefs

    def __call__(self, x):
        sum_f = 0
        for i in range(self.power + 1):
            sum_f += (x ** (self.power - i)) * self.coefs[i]
        return sum_f

    def __str__(self):
        description = f'{self.coefs[0]}x^{self.power}'
        for i in range(1, self.power):
            description += f" + {self.coefs[i]}x^{self.power - i}"
        description += f' + {self.coefs[-1]}'
        description += " = 0"
        return description


class Derivative(Function):
    def __init__(self, f: Function):
        new_coefs = []
        old_coefs = f.coefs[:-1]
        for i in range(f.power):
            new_coefs.append((f.power - i) * old_coefs[i])
        super().__init__(new_coefs)
