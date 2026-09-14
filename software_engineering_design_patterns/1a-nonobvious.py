raw = {}
ds = load(fp)
for n, X in ds.items():
    for mtr in fns:
        raw[n] = mtr(X)
res = Result(raw)
res.write(fpo)
