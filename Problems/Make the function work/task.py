def closest_mod_5(x):
    if x % 5 == 0:
        return x
    a = x % 5
    return x + (5 - a)


xa = 45
closest_mod_5(xa)
