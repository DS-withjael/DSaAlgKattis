from itu.algs4.fundamentals.stack import Stack

def main():
    w = Stack()
    inp = input()
    balances = {")": "(", "]" : "["}
    for i in inp:
        if i == "[" or i == "(":
            w.push(i)
        elif i == "]" or i == ")":
            if w.size() == 0:
                return False
            elif w.pop() != balances[i]:
                return False
            else:
                continue
        else:
            return False

    if w.size() == 0:
        return True
    else:
        return False

if main() == True:
    print("1")
else:
    print("0")