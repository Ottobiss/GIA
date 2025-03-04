counter = 0

with open('data.csv') as f:
    for i, s in enumerate(f, 1):
        s = sorted(list(map(int, s.split(';'))))

        if (s[0] + s[-1]) == (s[1] + s[2]) > 2 * s[3] - s[0]:
            counter += 1

print(counter)
