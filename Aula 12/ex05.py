def tem_igual(*args):
    for i in range(len(args)-1):
        n = args[i]
        for i in range(i+1, len(args)):
            if args[i] == args[j]:
                return True
    return false

print(tem_igual(1,2,4,3,5,3))