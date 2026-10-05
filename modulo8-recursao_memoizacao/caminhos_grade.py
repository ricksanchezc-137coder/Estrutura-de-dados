from functools import cache

chamadas = 0


def caminhos_ingenuo(l, c):
    global chamadas
    chamadas += 1
    if l == 0 or c == 0:
        return 1
    return caminhos_ingenuo(l - 1, c) + caminhos_ingenuo(l, c - 1)


@cache
def caminhos_cache(l, c):
    if l == 0 or c == 0:
        return 1
    return caminhos_cache(l - 1, c) + caminhos_cache(l, c - 1)


for n in (2, 6, 8, 10):
    chamadas = 0
    caminhos_cache.cache_clear()
    r1 = caminhos_ingenuo(n, n)
    r2 = caminhos_cache(n, n)
    print(f"grade {n}x{n}: caminhos={r1} | iguais={r1 == r2} | chamadas sem cache={chamadas}")
    print("  ", caminhos_cache.cache_info())

caminhos_cache.cache_clear()
r = caminhos_cache(100, 100)
print(f"grade 100x100: {len(str(r))} dígitos")
print("  ", caminhos_cache.cache_info())
