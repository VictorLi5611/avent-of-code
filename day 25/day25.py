
lines = [line.rstrip('\n') for line in open("input.txt" ,"r")]
a, b = [int(i) for i in lines]

def root(a):
    count = 0
    for i in range(100000000):
        count += 1 
        if pow(7, i, 20201227) == a:
            print(count)
            return i

print(pow(a, root(b), 20201227))

