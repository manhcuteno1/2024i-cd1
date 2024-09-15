arr = []
n, k = -1, -1
with open("tiamang.inp", "r") as file:
    for line in file:
        if n == -1:
            n, k = line.split()
            n, k = int(n), int(k)
        else:
            x = int(line)
            arr.append(x)

frequency = {}
res = []
for x in arr:
    if x not in frequency:
        frequency[x] = 0
    frequency[x] += 1
    if frequency[x] <= k:
        res.append(x)

with open("tiamang.out", "w") as file:
    for x in res:
        file.write(f"{x}\n")


