
def kolmioluku(luku, aloituspiste=1):
    mahdolliset = []
    while aloituspiste ** 2 - 1 < luku:
        temp_summa = []
        temp = aloituspiste
        while sum(temp_summa) < luku:
            temp_summa.append(temp)
            temp += 1
            if sum(temp_summa) == luku:
                mahdolliset.append(temp_summa)
        aloituspiste += 1
    return mahdolliset



def prettyPrint(mahdolliset):
    master_temp = []
    for i in mahdolliset:
        temp = ''
        for a in i:
            temp += str(a)
            temp += ' + '
        temp = temp[:len(temp) - 3]
        master_temp.append(temp)
    return '\n\t'.join(master_temp)


for i in range(100):
    if not kolmioluku(i):
        continue
    print('{}:\t{}\n'.format(i, prettyPrint(kolmioluku(i))))
