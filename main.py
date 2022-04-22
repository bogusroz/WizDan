#ZESTAW A

#Zad.1
def funkcjaSlownik(slownik):
    lista = []
    for key in slownik.keys():
        if type(slownik[key]) == int:
            lista.append(key)
    return lista

slownik = {1: 2, "a": 3, 4.5: 1, 2: "a"}
print(funkcjaSlownik(slownik))

print()
#Zad.2
plik = open("tekst.txt", 'r', encoding='utf-8')
plik.seek(24)
znaki = plik.read(20)
plik.close()
duze = 0
for znak in znaki:
    if znak.isupper():
        duze += 1
if duze > 0:
    print("Duzych znakow jest: " + str(duze))
else:
    print("Nie ma duzych znaków")

print()
#Zad.3
lista=[1,3,4,15,10,1,25,17]
lista2 = [lista[i] for i in range(0, len(lista), 2)]      #range -> (start, stop, step)

print(lista)
print(lista2)
print()

#Zad.4
w = pow(pi, 3) + pow((log2(64) + sin(45)), 1/4)
print(round(w, 2))

#Zad.5
try:
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    wynik = a**b
    plik = open("zadanie5v2.txt", 'w+')
    plik.write(str(wynik))
    plik.close
except ValueError:
    print("Nie podano liczby calkowitej")



#ZESTAW B

#Zad.1
plik = open('tekst.txt', 'r', encoding='utf-8')
plik.seek(63)
znaki = plik.read(42)

for znak in znaki:
    male = 0
    for znak in znaki:
        if znak.islower():
            male += 1
if male > 0:
    print("Malych znakow jest: " + str(male))
else:
    print("Nie ma malych znakow")
print()

#Zad.2
def liczby(lista):
    lista2 = []
    for x in lista:
        if (type(x) == int) | (type(x) == float):
            lista2.append(x)
    return lista2, max(lista2), min(lista2)

lista = ['a', 4, 5.55, 'b', 2, 1]
print(liczby(lista))

#Zad.3
try:
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    jedynka = (pow(sin(a),2) + pow(cos(b),2))
    plik = open('zadanie3.txt', 'w+')
    if jedynka == 1:
        plik.write("Jest to jedynka trygonometryczna")
    else:
        plik.write("Nie jest to jedynka trygonometryczna")
    plik.close
except ValueError:
    print("Nie podano liczby calkowitej")

#Zad.4
lista = [1,3,4,5,1,6,8,10,7,12,5]
lista2 = [x for x in lista if x > lista[-1]]
print(lista)
print(lista2)
print()

#Zad.5
w = pow(e,3) + pow( log(pow(cos(36),2) + pi ) ,1/5)
print(w)
print(round(w, 2))
