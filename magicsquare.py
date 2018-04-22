from itertools import combinations, combinations
import random
combs = []
dictcomb = {}
lis = [3, 9, 8, 2, 5, 6, 7, 1, 47, 16, 48, 49, 43, 19, 36, 42, 17, 41, 10, 35, 29, 12, 37, 20, 44, 45, 40, 30, 15, 21,
       38, 13, 31, 14, 34, 33]
for i in (5, len(lis)):
    for comb in combinations(lis, i):
        if sum(comb) == 107:
            # print(comb, '= 107')
            combs.append(comb)
            dictcomb.setdefault(107,[]).append(comb)
    print("Completed 107")
    for comb in combinations(lis, i):
        if sum(comb) == 113:
            # print(comb, '= 113')
            combs.append(comb)
            dictcomb.setdefault(113, []).append(comb)
    print("Completed 113")
    for comb in combinations(lis, i):
        if sum(comb) == 119:
            # print(comb, '= 119')
            combs.append(comb)
            dictcomb.setdefault(119, []).append(comb)
    print("Completed 119")
    for comb in combinations(lis, i):
        if sum(comb) == 131:
            # print(comb, '= 131')
            combs.append(comb)
            dictcomb.setdefault(131, []).append(comb)
    print("Completed 131")
    for comb in combinations(lis, i):
        if sum(comb) == 137:
            # print(comb, '= 137')
            combs.append(comb)
            dictcomb.setdefault(137, []).append(comb)
    print("Completed 137")
    for comb in combinations(lis, i):
        if sum(comb) == 143:
            # print(comb, '= 143')
            combs.append(comb)
            dictcomb.setdefault(143, []).append(comb)
    print("Completed 143")
    for comb in combinations(lis, i):
        if sum(comb) == 149:
            # print(comb, '= 149')
            combs.append(comb)
            dictcomb.setdefault(149, []).append(comb)
    print("Completed 149")
    for comb in combinations(lis, i):
        if sum(comb) == 141:
            # print(comb, '= 141')
            combs.append(comb)
            dictcomb.setdefault(141, []).append(comb)
    print("Completed 141")
    for comb in combinations(lis, i):
        if sum(comb) == 133:
            # print(comb, '= 133')
            combs.append(comb)
            dictcomb.setdefault(133, []).append(comb)
    print("Completed 133")
    for comb in combinations(lis, i):
        if sum(comb) == 117:
            # print(comb, '= 117')
            combs.append(comb)
            dictcomb.setdefault(117, []).append(comb)
    print("Completed 117")
    for comb in combinations(lis, i):
        if sum(comb) == 109:
            # print(comb, '= 109')
            combs.append(comb)
            dictcomb.setdefault(109, []).append(comb)
    print("Completed 109")
    for comb in combinations(lis, i):
        if sum(comb) == 101:
            # print(comb, '= 101')
            combs.append(comb)
            dictcomb.setdefault(101, []).append(comb)
    print("Completed 101")


for i in (6, len(lis)):
    for comb in combinations(lis, i):
        if sum(comb) == 150:
            # print(comb, '= 150')
            combs.append(comb)
            dictcomb.setdefault(150, []).append(comb)
    print("Completed 150")

combs = [item for sublist in combs for item in sublist] # flatten it.
combs = list(set(combs)) # removes duplicates.

# print(combs)
#       0	1	2	3	4
# 5		    6	7	8		9
# 10	11		12		13	14
# 15	16	17		18	19	20
# 21	22		23		24	25
# 26		27	28	29		30
# 	    31	32	33	34	35

col1 = [5,10,15,21,26]
col2 = [0,11,16,22,31]
col3 = [1,6,17,27,32]
col4 = [2,7,12,23,28,33]
col5 = [3,8,18,29,34]
col6 = [4,13,19,24,35]
col7 = [9,14,20,25,30]
lin1 = list(range(0,5))
lin2 = list(range(5,10))
lin3 = list(range(10,15))
lin4 = list(range(15,21))
lin5 = list(range(21,26))
lin6 = list(range(26,31))
lin7 = list(range(31,36))

genes = [col1,col2,col3,col4,col5,col6,col7,lin1,lin2,lin3,lin4,lin5,lin6,lin7]
resultados = [107,113,119,150,131,137,143,149,141,133,150,117,109,101]
def soma(pos,combs):
    soma = 0
    for i in pos:
        soma += combs[i]
    return soma

final = False
while not final:
    for i, gene in enumerate(genes):
        if resultados[i] == soma(gene,combs):
            print("i = ", i, "comb:", combs) if i > 2 else None
            if i == len(genes)-1:
                final = True

        else:
            random.shuffle(combs)
            break

