import copy

def compressValue(v, v_bar):

    low = 0
    high = len(v_bar) - 1

    while low <= high:
        mid = (low + high)//2
        if (v == v_bar[mid]):
            return mid
        elif (v > v_bar[mid]):
            low = mid + 1
        else:
            high = mid - 1

        if low > high:
            return low - 1



def makeTree(a,v, tl, tr, b):

    if (tl == tr):
        b[v] = a[tl]
    else:
        tm = (tl + tr) // 2
        makeTree(a, v*2, tl, tm, b)
        makeTree(a, v*2+1, tm+1, tr, b)
        b[v] = b[v*2] + b[v*2 + 1]


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

def requestTreeLinks(x1, x2, tree_mod_links, n):
    tree = tree_mod_links[x1]

    return getNode(1, x2, 0, n - 1, tree)


def getNode(node, x, l, r, b):

    if (l == r):
        return b[node]
    else:
        mid = (l + r) // 2
        if (x <= mid):
            return b[node] + getNode(node * 2, x, l, mid, b)
        else:
            return b[node] + getNode((node * 2) + 1, x, mid+1, r, b)



#[l, r)
def changeMod(node, begin, end, l, r, x):

    if (l > r):
        return 0

    if (l == begin and r == end):
        mod[node] += x

    else:
        mid = (begin + end) // 2
        changeMod(node * 2, begin, mid, l, min(r, mid), x)
        changeMod(node * 2 + 1, mid + 1, end, max(l, mid+1), r, x)



n = int(input())
points = []
x_bar = set([])
y_bar = set([])
y_events = []
dict = {}
dict_x = {}
counter = 0
for i in range(n):

    x1, y1, x2, y2 = map(int, input().split())
    x_bar.add(x1)
    y_bar.add(y1)
    x_bar.add(x2)
    y_bar.add(y2)

    y_events.append([y1, y2, 1])
    y_events.append([y1, y2, -1])

    points.append([x1, y1])
    points.append([x2, y2])

x_bar = list(x_bar)
y_bar = list(y_bar)
x_bar.sort()
y_bar.sort()

y_events.sort(key=lambda x: (-x[2], x[1] if x[2] < 0 else x[0], x[0] if x[2] < 0 else x[1]))

for i in range(len(y_bar)):
    dict[y_bar[i]] = i

for i in range(len(x_bar)):
    dict_x[x_bar[i]] = i

for i in range(len(y_events)):
    y_events[i][0] = dict.get(y_events[i][0])
    y_events[i][1] = dict.get(y_events[i][1])

nodes = len(x_bar) - 1
tree_links = [None] * len(x_bar)
tree_mod_links = [None] * len(y_events)

b = [0] * len(y_bar) * 2**2

for i in range(len(y_bar)):
    b[i] = y_bar[i]

makeTree(y_bar, 1, 0, len(y_bar) - 1, b)
mod = [0] * len(b)

counter = 0
for event in y_events:
    x1 = event[0]
    x2 = event[1]

    changeMod(1, 0, len(y_bar) - 1, x1, x2, event[2])
    tree_mod_links[counter] = copy.deepcopy(mod)
    counter += 1

n = int(input())
ans = ""
for i in range(n):
    x1, x2 = map(int, input().split())

    if dict_x.get(x1) == None:
        x1 = x_bar[compressValue(x1, x_bar)]
    if dict.get(x2) == None:
        x2 = y_bar[compressValue(x2, y_bar)]

    x1 = dict_x.get(x1)
    x2 = dict.get(x2)

    ans += str(requestTreeLinks(x1, x2, tree_mod_links, len(y_bar))) + " "

print(ans)