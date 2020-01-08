def random_walk(N):
    rw = [1]
    for _ in range(1, N):
        rw = [0.5*x + 0.5*y for x, y in zip(rw+[0, 0], [0, 0]+rw)]
    return rw