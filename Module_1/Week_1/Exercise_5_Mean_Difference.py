def md_nre_single_sample(y, y_hat, n, p):
    print(f"md_nre_single_sample(y={y}, y_hat={y_hat}, n={n}, p={p})")
    return print(f">> {(y ** (1 / n) - y_hat ** (1 / n)) ** p}\n")


md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)
md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)
md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1)
md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1)
