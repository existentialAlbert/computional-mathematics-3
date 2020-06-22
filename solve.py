import methods


def solve_equation():
    print('Введите коэффициенты')
    c = input()
    coefs = [float(x.strip()) for x in c.split()]
    function = methods.Function(coefs)
    eps = 0.01
    print('Введите интервал уточнения корня')
    a, b = input().split()
    a = float(a)
    b = float(b)
    try:
        if function(a) * function(b) > 0:
            print(
                "!Внимание: необходимое условие существования корней не выполнено. Результат может не являться приближенным корнем уравнения")
        bis_i, bis_x, bis_log = methods.bisection_method(a, b, function, eps)
        print(
            "Метод половинного деления \nКоличество шагов: {0}\nПолученное приближенное решение: {1}\nf(x*) = {2}".format(
                bis_i, bis_x, function(bis_x)))
        print(bis_log)
    except AssertionError as inst:
        print("Метод половинного деления: " + inst.args[0])
    print('Введите интервал уточнения корня')
    a, b = input().split()
    a = float(a)
    b = float(b)
    s_i, s_x, s_log = methods.secants_method(a, b, function, eps)
    print(
        "Метод секущих \nКоличество шагов: {0}\nПолученное приближенное решение: {1}\nf(x*) = {2}".format(
            s_i, s_x, function(s_x)))
    print(s_log)
    try:
        print('Введите интервал уточнения корня')
        a, b = input().split()
        a = float(a)
        b = float(b)
        fix_i, fix_x, fix_log = methods.simple_iteration_method(a, b, function, eps)
        print(
            "Метод простых итераций \nКоличество шагов: {0}\nПолученное приближенное решение: {1}\nf(x*) = {2}".format(
                fix_i, fix_x, function(fix_x)))
        print(fix_log)
    except AssertionError as inst:
        print("Метод простых итераций: " + inst.args[0])


if __name__ == "__main__":
    # print('Исходное уравнение: −1,38𝑥^3 − 5,42𝑥^2 + 2,57𝑥 + 10,95')
    # -1.38 -5.42 2.57 10.95
    solve_equation()
