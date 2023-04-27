import copy


def closestBinPow(x):
    i = 1
    while (i < x):
        i *= 2
    return i

def makeTree(a):
    for i in range(len(a), closestBinPow(len(a))):
        a.append(0)

    b = [0] * (len(a) * 2)

    for i in range(len(a)):
        b[i + len(a) - 1] = a[i]
    for i in range(len(a)-2, -1, -1):
        b[i] = b[2 * i + 1] + b[2 * i + 2]

    return b

#[l, r]
def requestTree(l, r, n, b):
    sum = 0
    l += n
    r += n

    while (l != 0):
        if (l % 2 != 0):
            sum += b[l - 1]
        if (r % 2 == 0):
            sum += b[r - 1]

        if (l == r):
            break

        l = l // 2
        r = (r - 1) // 2

    return sum

#[l, r)
def changeMod(l, r, n, mod, x):
    l += n
    r += n

    while (l < r):
        if (l % 2 > 0):
            mod[l - 1] += x
            l += 1
        if (r % 2 > 0):
            r -= 1
            mod[r - 1] += x

        l = l // 2
        r = r // 2



n = int(input())
points = []
x_bar = set([])
y_bar = set([])
x_events = []

for i in range(n):

    x1, y1, x2, y2 = map(int, input().split())
    x_bar.add(x1)
    y_bar.add(y1)
    x_bar.add(x2)
    y_bar.add(y2)

    x_events.append([x1, x2])

    points.append([x1, y1])
    points.append([x2, y2])

x_bar = list(x_bar)
y_bar = list(y_bar)
x_bar.sort()
y_bar.sort()

x_events.sort()
nodes = len(x_bar) - 1
tree_links = [None] * len(x_bar)
tree_mod_links = [None] * len(x_bar)
b = makeTree(x_bar)
mod = [0] * len(b)

print(x_events)
print(requestTree(0, 5, len(b) // 2, b))
changeMod(1, 3, len(mod) // 2, mod, 1)

counter = 0
for event in x_events:
    x1 = event[0]
    x2 = event[1]

    changeMod(x1, x2, len(mod) // 2, mod, 1)
    tree_links[counter] = copy.deepcopy(b)
    tree_mod_links[counter] = copy.deepcopy(mod)
    counter += 1


print(tree_mod_links)