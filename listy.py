zwierzeta = ['kot', 'pies', 'kon', 'krowa']
print(zwierzeta[2])
print(zwierzeta)
print(zwierzeta[len(zwierzeta)-1])
print(zwierzeta[-1])
print(zwierzeta[-2])
zwierzeta.append('slon')
print(zwierzeta)
zwierzeta.insert(1, 'kura')
print(zwierzeta)
print(len(zwierzeta))

print(zwierzeta.index('kon'))
zwierzeta.remove('kura')
print(zwierzeta)

zwierzeta.pop(3)
print(zwierzeta)
zwierzeta.sort()
print(zwierzeta)

zwierzeta.reverse()
print(zwierzeta)

noweZwierzeta = ['pingwin', 'zebra', 'zyrafa']
zwierzeta.extend(noweZwierzeta)
print(zwierzeta)

print(noweZwierzeta)
zoo = noweZwierzeta
print(zoo)
noweZwierzeta.clear()
print(noweZwierzeta)
print(zoo)

a = 5
b = 7
print(a, b)
a, b=b, a
print(a, b)
print((a, b))
krotka=(5, 7, 8, 3)
print(krotka.index(2))