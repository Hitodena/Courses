def avg(fn):
    def wrap(*arg):
        a = ''
        for i in arg:
            a += str(i) + ", "
        print("Среднее арифметическое:", a , "=", fn(*arg) / len(arg))

    return wrap


@avg
def summa(*args):
    print("Сумма чисел:", *args, "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)