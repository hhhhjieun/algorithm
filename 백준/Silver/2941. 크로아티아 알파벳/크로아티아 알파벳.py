word = input()

# 크로아티아
cros = [['c', '='], ['c', '-'], ['d', '-'], ['l', 'j'], ['n', 'j'],
              ['s', '='], ['z', '=']]

total = len(word)

for i in range(total - 1):
    test = [word[i] , word[i + 1]]

    for j in range(6):
        if test == cros[j]:
            total -= 1

    if test == ['z', '=']:
        if i >= 1 and word[i -1] == 'd':
            total -= 2
        else:
            total -= 1

print(total)