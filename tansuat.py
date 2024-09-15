arr = []
n = -1
with open("numbers.inp", "r") as file:
    for line in file:
        if n == -1:
            n = int(line)
        else:
            x = int(line)
            arr.append(x)

frequency = {}
for x in arr:
    if x not in frequency:
        frequency[x] = 0
    frequency[x] += 1

with open("numbers.out", "w") as file:
    for number, freq in frequency.items():
        if freq > 1:
            file.write(f"{number} {freq}\n")
