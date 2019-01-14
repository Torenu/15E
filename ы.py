n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]


def check_buy(i, c, d): # 0 если чел не доходит до нас, c если да
    if c in d[i + 1:]:
        return 0
    else:
        return c


def pribil(i, c, n, a, b):    # ищем прибыль нашего магаза со ста человек
    p = 0   # прибыль
    d = a[:i] + [c] + a[i:]  # итоговый список магазов с ценами
    for k in range(1, n):       # k - терпение покупателя
        if k >= i and c == min(d[:k + 1]):
            p += b[k] * check_buy(i, c, d[:k + 1])
    d = d[::-1]
    i = n - i
    for k in range(1, n):
        if k >= i and c == min(d[:k + 1]):
            p += b[k] * check_buy(i, c, d[:k + 1])
    return p


p = []
for i in range(1, n):   # позиция магаза
    for c in range(1, max(a) + 1):  # цена от 1 до максимального
        p.append([pribil(i, c, n, a, b), str(i), str(c)])
print(' '.join(sorted(p)[-1][1:]))

# ъаэ
