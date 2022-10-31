def func(w1,w2):
    if w2 != 0:
        return func(w2,w1%w2)
    else:
        return w1

if __name__ == "__main__":
    pairs = []
    m = input(" [+] enter modulo: ")

    for i in range(0,m):
        pairs.append([i,m])

    for pair in pairs:
        ggT = func(pair[0],pair[1])
        if ggT != 1:
            print(pair, "hat keine multiplikative inverse")
    
