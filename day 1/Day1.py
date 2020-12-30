lst = []
with open ("input.txt", "r") as f:
    for line in f:
        lines = line.strip()
        lst.append(int(lines))



for i in range (len(lst)):
    for j in range (len(lst)):
        for l in range(len(lst)):
            if lst[i] + lst[j] + lst[l] == 2020:
                print(lst[i]*lst[j]*lst[l])