def simpson(y_vals, h):
    # y_vals: data of isocontours, e.g. areas of isocontours, see Table 4.3 for example
    # h: difference between isocontours, regular space, see Table 4.3 for example
    i = 1
    total = y_vals[0] + y_vals[-1]
    for y in y_vals[1:-1]:
        if i % 2 == 0:
            total += 2 * y
        else:
            total += 4 * y
        i += 1
    return total * (h / 3.0)
