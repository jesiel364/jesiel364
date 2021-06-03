cor = []
a = input('rga:').replace(' ','')
b = []
def convert(a):
        print(a[0:3])
        print(a[4:7])
        print(a[8:12])
        cor.append((a[0:3]))
        cor.append((a[4:7]))
        cor.append((a[8:12]))

        for n in cor:
                b.append(n + '/' + '255')

convert(a)

print('Código de cor para Kivy/Python')
print('{}{}{}{}'.format(b[0] + ',',b[1]+',',b[2]+',','1'))
print(len(a))
