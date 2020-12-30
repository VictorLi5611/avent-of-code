from collections import defaultdict

f = open("input.txt", "r")
lines = f.read().split("\n")
lines = [l for l in lines if len(l) > 0]

grid = defaultdict(bool)

def shift(p, d):
  x, y, z = p
  if d == "e":
    return (x+1,y-1,z)
  if d == "w":
    return (x-1,y+1,z)
  if d == "ne":
    return (x+1,y,z-1)
  if d == "nw":
    return (x,y+1,z-1)
  if d == "se":
    return (x,y-1,z+1)
  if d == "sw":
    return (x-1,y,z+1)

for line in lines:
  p = (0, 0, 0)
  while line:
    if line.startswith("n") or line.startswith("s"):
      d = line[:2]
      line = line[2:]
      p = shift(p, d)
    else:
      d = line[:1]
      line = line[1:]
      p = shift(p, d)
  grid[p] = not grid[p]

count = 0
for v in grid.values():
  if v:
    count += 1
print(count)