"""a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(a[i])


for i in range (100):
    if i % 2 != 0:
        print(i)

"""

contraseña =input('¿tu contraseña?:')
lonfitud = len(contraseña)
for i in contraseña:
    if lonfitud < 8:
        print('error')
    elif contraseña[i] == " ":
        print('error')
    else:
        print('ok')