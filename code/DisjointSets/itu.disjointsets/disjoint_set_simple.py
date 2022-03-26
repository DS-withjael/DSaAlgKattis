from itu.algs4.fundamentals.uf import UF
# code inspired by code found in union function built into itu.algs4 library

def query(s, t):
    if disjoint_set.find(s) == disjoint_set.find(t):
        print("1")
    else:
        print("0")

def union1(s, t):
    if disjoint_set.find(s) == disjoint_set.find(t):
        return
    else:
        disjoint_set._parent[disjoint_set.find(s)] = disjoint_set.find(t)

def move(s, t):
    if disjoint_set.find(s) == disjoint_set.find(t):
        return
    else:
        counter = 0
        disjoint_set._parent[s] = disjoint_set._parent[t]
        for i, j in enumerate(disjoint_set._parent):
            if j == s:
                if counter == 0:
                    new_parent = i
                    disjoint_set._parent[i] = new_parent
                    counter += 1
                else:
                    disjoint_set._parent[i] = new_parent

def main():
    singletons, operations = input().strip().split()
    global disjoint_set
    disjoint_set = UF(int(singletons))
    # print(disjoint_set._parent)
    for i in range(0, int(operations)):
        operation, s, t = input().strip().split()
        if operation == "0":
            query(int(s), int(t))
            # print(disjoint_set._parent)
        if operation == "1":
            union1(int(s), int(t))
            # print(disjoint_set._parent)
        if operation == "2":
            move(int(s), int(t))
            # print(disjoint_set._parent)


if __name__ == "__main__":
    main()