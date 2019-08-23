def alpha(args):

    args.append(33)

    def betta(itm):
        nonlocal args
        args.append(itm)
        return args

    return betta


items = [1, 2, 3]
print(items)

g = alpha(items)
print(items)
items.append(555)
t = g(66)

print(items)
print(t)
