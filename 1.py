import itertools
alphabet = "ТИМОФЕЙ"
ar = itertools.product(alphabet, repeat=5) 
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    flag = True
    for i in range(len(e) - 1):
        if e.count('Й') > 1 or e[0] == 'Й' or e[-1] == 'Й' or (e[i] == 'Й' and e[i + 1] == 'И') or (e[i + 1] == 'Й' and e[i] == 'И'):
            flag = False
    if flag == True: count += 1
print(count)