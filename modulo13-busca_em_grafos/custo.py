import timeit
from bfs import bfs
from dfs import dfs_iterativo, dfs_recursivo


def cadeia(n):
    g = {i: [] for i in range(n)}
    for i in range(n - 1):
        g[i].append(i + 1)
        g[i + 1].append(i)
    return g


def tempo(f, g):
    return min(timeit.repeat(lambda: f(g, 0), number=1, repeat=5))


if __name__ == "__main__":
    print("n | bfs | dfs_iterativo")
    for n in [25000, 50000, 100000, 200000, 400000]:
        g = cadeia(n)
        print(n, f"{tempo(bfs, g):.4f}", f"{tempo(dfs_iterativo, g):.4f}")

    print("recursivo vs iterativo na cadeia:")
    for n in [500, 900, 1000, 5000]:
        g = cadeia(n)
        try:
            r = dfs_recursivo(g, 0)
            rec = f"ok, {len(r)} vertices"
        except RecursionError:
            rec = "RecursionError"
        it = dfs_iterativo(g, 0)
        print(n, "recursivo:", rec, "| iterativo:", len(it), "vertices")
