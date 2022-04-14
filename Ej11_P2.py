f=open("nombres_1.txt", "r", encoding="utf-8")

nombresuno =f.read().replace(',', ' ').split()
f.close()
f=open("nombres_2.txt", "r", encoding="utf-8")
nombresdos = f.read().replace(',', ' ').split()
f.close()
f=open("eval1.txt", "r", encoding="utf-8")
eval1 = f.read().replace(',', ' ').split()
f.close()
f=open("eval2.txt", "r", encoding="utf-8")
eval2 = f.read().replace(',', ' ').split()
f.close()
print()
print('Estos nombres que se encuentran en ambos archivos:')
nombresEnAmbos = []
for n in nombresuno :
    if n in nombresdos :
        nombresEnAmbos.append(n)    
print(nombresEnAmbos)


print()
print('   {:<10}  {:>8} {:>8} {:>8}'.format('Nombre', 'Eval1', 'Eval2', 'Total'))
for i, valor in enumerate(zip(nombresuno, eval1, eval2)) :
    print('{:>2} {:<15} {:<8} {:<8} {:<8}'.format(i, valor[0], valor[1], valor[2], int(valor[1]) + int(valor[2])))
letra = input("Ingresa una letra para finalizar")
