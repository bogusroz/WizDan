import sys
import math
#Zadania domowe Lab1

# #Zad.1
# a = "string 1"
# b = "string 2"
# c = 13
# d = 12
# e = 1.2
# f = 6.41
# g = 5+2j
# h = 8+4j
# print(a,b,c,d,e,f,g,h)

# #Zad.2
# a = input("Podaj pierwsza liczbe: ")
# oper = input("Jakie dzialanie chcesz wykonac? ")
# b = input("Podaj druga liczbe: ")
# a = int(a)
# b = int(b)
# if oper=='+':
#     wynik = a+b
# elif oper=='-':
#     wynik = a-b
# elif oper=='*':
#     wynik = a*b
# elif oper=='/':
#     wynik = a/b
# print(wynik)

# #Zad.3

# #Zad.4
# a = math.e**10
# b = (math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6))
# c = math.floor(3.55)
# d = math.ceil(4.80)
# print(a,b,c,d)

# #Zad.5
# imie = "BOGUMIŁ"
# nazwisko = "RÓŻAŃSKI"
#
# imie = imie.capitalize()
# nazwisko = nazwisko.capitalize()
# print(imie, nazwisko)

# #Zad.6
# tekst = "la la baba ka la la"
# policz = tekst.count("la")
# print(policz)

# #Zad.7
# a = "To jest łańcuch"
# print(a[1],a[-1])

# #Zad.8
# tekst = "la la baba ka la la"
# podziel = tekst.split()
# print(podziel)

# #Zad.9
# str = "Format"
# fl = 2.22
# print(str, fl)
# print(hex(0XFF))
# szesnstkowa = 0x1f
# print('{0:x}'.format(szesnstkowa))

#==========================================================================
import sys
import math
#ZADANIA DOMOWE LISTA LAB2

# #Zad. 1
# sporty = ["Rower", "Bieganie", "Pływanie", "Piłka nożna"]
# sporty.reverse()
# sporty.append("Koszykowka")
# sporty.append("Piłka ręczna")
# print(sporty)
#
# #Zad. 2
# slownik = {"itd." : "i tak dalej",
#            "ww." : "wyzej wymienione",
#            "ds." : "do spraw"}
# print(slownik)
#
# #Zad. 3
# slownik2 = {"GTA" : "Grand Theft Auto",
#             "exp." : "Experience Points",
#             "HP" : "Health Points"}
# for a in slownik2:
#     print(a)

# #Zad. 4
# ile=0
# zdanie=input("Wpisz zdanie: ")
# for x in zdanie:
#     if x == 'a':
#         ile+=1
# print(ile)

# #Zad. 5 #jak tutaj uzyc readline i write?
# a = float(input("Podaj liczbe a: "))
# b = float(input("Podaj liczbe b: "))
# c = float(input("Podaj liczbe c: "))
# wynik = a**b + c
# print(wynik)

# #Zad. 6
# a = float(input("Podaj pierwsza liczbe: "))
# b = float(input("Podaj druga liczbe: "))
# c = float(input("Podaj trzecia liczbe: "))
# if (a > b) and (a > c):
#     maks = a
# elif (b > a) and (b > c):
#     maks = b
# else:
#     maks = c
# print("Najwieksza liczba jest ", maks)

# #Zad. 7
# liczby = [1, 2.2, 3, 4.4, 5, 6.6, 7, 8.8, 9]
# #for a in liczby:
# liczby2 = [x**2 for x in liczby]
# print(liczby2)

# #Zad. 8
# parzyste = []
# x = 0
# while x !=10:
#     x += 1
#     if x%2==0:
#         parzyste.append(x)
# print(parzyste)

# #Zad. 9
# liczba = input("Podaj liczbę nieujemną: ")
# liczba = float(liczba)
# if liczba>0:
#     print(math.sqrt(liczba))
# else:
#     print("Podana liczbę ujemną")

# try:
#     print(math.sqrt(liczba))
# except : #co tu dac
#     print("Podana liczbę ujemną")

        

#==========================================================================
import sys
import math
import random
#PRACA DOMOWA LAB3

# #Zad. 1
# a = []
# for x in range(1,11):
#     a.append(1-x)
# print(a)
#
# b = []
# for y in range(8):
#     b.append(4**y)
# print(b)
#
# c = []
# for z in b:
#     if z % 2 == 0:
#         c.append(z)
# print(c)

# #Zad. 2
# lista1 = []
# i=1
# while i<11:
#     x = (random.randint(0, 30))
#     lista1.append(x)
#     i+=1
# print(lista1)
#
# lista2 = []
# for y in lista1:
#     if y % 2 == 0:
#         lista2.append(y)
# print(lista2)

# #Zad. 3
# slownik = {'szt.' : ["Mango", "Pączek", "Bluza"],
#            'litr' : ["Pepsi","Olej"],
#            'kg' : ["Mąka","Banany"]}
# # print(slownik)
# # sztuki = []
# # for key in slownik.items():
# #     if key == 'szt.'
# #         sztuki.append(values)
# sztuki =  [slownik[x] for x in slownik.keys() if x=='szt.']
# print(sztuki)

# #Zad. 4
# def trojkat_prostokatny(a,b,c):
#     wzor = (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)
#
#     if wzor:
#         print("Trojkąt jest prostokątny!")
#         return 1
#     else:
#         print("Trojkąt nie jest prostokątny!")
#         return 0
# print(trojkat_prostokatny(3,4,5))
# print(trojkat_prostokatny(5,4,3))
# print(trojkat_prostokatny(4,6,8))

# #Zad. 5
# def pole_trapezu (a,b,h):
#     pole = ((a+b)*h)/2
#     return pole
# print(pole_trapezu(4,6,8))

# #Zad. 6
# def iloczyn(a=1,b=4,ile=10):
#   for i in range (ile):
#     a*=b
#   return a
# print(iloczyn())

# #Zad. 7
# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         for a in range(1, len(liczby), 1):
#             iloczyn_liczb *= b
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))

# #Zad. 8
# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow,2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))


# #Zad. 9
print(arytmetyczny.n_ty_wyraz(6, 6, 2))
print(arytmetyczny.suma_ciagu(6, 16, 6))
print(geometryczny.n_ty_wyraz(1, 4, 11))

import ciagi.arytmetyczny
from ciagi import

# # Pliki w folderze projektu - Nazwa i pozniej zawartosc

#__init__.py
#__all__ = ['arytmetyczny', 'geometryczny']


#arytmetyczny.py
#def n_ty_wyraz(a1, n, r):
#    return a1 + (n-1)*r

#def suma_ciagu(a1, an, n):
#    return (a1+an)/2*n


#geometryczny.py
# def n_ty_wyraz(a1, q, n):
#     return a1 * q**(n-1)
# 
# def suma(a1, n, q):
#     if q == 1:
#         return a1*n
#     else:
#         return a1 * (1-q**n)/(1-q)

#==========================================================================
import sys
import math
#PRACA DOMOWA LAB4

# #Zad.1
# liczby=[]
# for x in range(0,31):
#     liczby.append(x * 2)
# file = open("pomnozone.txt", "w+")
# file.write(str(liczby))
# file.close()

# #Zad.2
# with open('pomnozone.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')

# #Zad.3
# print("Wpisz kilka linijek tekstu")
# linijki = sys.stdin.readline()
# plik = open('linijki.txt', 'w+')
# plik.write(linijki)
# plik.close()
#
# with open('linijki.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')

# #Zad.4
#class NaZakupy():
#     """Zakupy"""
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#             self.nazwa_produktu = nazwa_produktu
#             self.ilosc = ilosc
#             self.jednostka_miary = jednostka_miary
#             self.cena_jed  = cena_jed
# 
#     def wyswietl_produkt(self):	# nie dziala
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#     def wyswietl_produkt(self):
#		  print("%(zm1)s  %(zm2)s%(zm3)s kosztuje %(zm4)s zl" % {'zm1': self.nazwa_produktu, 'zm2': self.ilosc, 'zm3': self.jednostka_miary, 'zm4': self.cena_jed})
#     def ile_produktu(self):
#         print(str(self.ilosc) + " " + self.jednostka_miary)
#     def ile_kosztuje(self):
#         kwota = self.cena_jed * self.ilosc
#         print(kwota)
# 
# zakup = NaZakupy("Ziemniaki",3,"kg",2)
# #zakup.wyswietl_produkt()   #dlaczego wyrzuca błąd?
# zakup.ile_produktu()
# zakup.ile_kosztuje()


class NaZakupy():
    """Zakupy"""
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
            self.nazwa_produktu = nazwa_produktu
            self.ilosc = ilosc
            self.jednostka_miary = jednostka_miary
            self.cena_jed  = cena_jed

    # def wyswietl_produkt(self):	# nie dziala
    #     print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def wyswietl_produkt(self):
        print("{}, {}{} w cenie {} zł za {}" .format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed, self.jednostka_miary))
#    def wyswietl_produkt(self):
#		  print("%(zm1)s  %(zm2)s%(zm3)s kosztuje %(zm4)s zl" % {'zm1': self.nazwa_produktu, 'zm2': self.ilosc, 'zm3': self.jednostka_miary, 'zm4': self.cena_jed})
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
    def ile_kosztuje(self):
        kwota = self.cena_jed * self.ilosc
        print(kwota)

zakup = NaZakupy("Ziemniaki",3,"kg",2)
zakup.wyswietl_produkt()   #dlaczego wyrzuca błąd?
zakup.ile_produktu()
zakup.ile_kosztuje()



# Zad.5
# class Ciagi:

# #Zad. 6
# class Robaczek:
#     x = 0
#     y = 0
#     krok = 1
#
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += (ile_krokow * self.krok)
#     def idz_w_dol(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
#     def idz_w_prawo(self, ile_krokow):
#         self.x += (ile_krokow * self.krok)
#     def idz_w_lewo(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
#
#     def pokaz_gdzie_jestes(self):
#         print("Robaczek znajduje się na współrzędnych x = " + str(self.x) + " i y =" + str(self.y))
#
# ruch = Robaczek(0, 0, 1) #pozycja startowa i wielkosc kroku robaczka
#
# ruch.idz_w_prawo(3)
# ruch.idz_w_lewo(7)
# ruch.idz_w_gore(1)
# ruch.idz_w_dol(2)
# ruch.pokaz_gdzie_jestes()




* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

Te same zadania tylko niezakomentowane



Zadania domowe Lab1

#Zad.1
a = "string 1"
b = "string 2"
c = 13
d = 12
e = 1.2
f = 6.41
g = 5+2j
h = 8+4j
print(a,b,c,d,e,f,g,h)

#Zad.2
a = input("Podaj pierwsza liczbe: ")
oper = input("Jakie dzialanie chcesz wykonac? ")
b = input("Podaj druga liczbe: ")
a = int(a)
b = int(b)
if oper=='+':
    wynik = a+b
elif oper=='-':
    wynik = a-b
elif oper=='*':
    wynik = a*b
elif oper=='/':
    wynik = a/b
print(wynik)

#Zad.3

#Zad.4
a = math.e**10
b = (math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6))
c = math.floor(3.55)
d = math.ceil(4.80)
print(a,b,c,d)

#Zad.5
imie = "BOGUMIŁ"
nazwisko = "RÓŻAŃSKI"

imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie, nazwisko)

#Zad.6
tekst = "la la baba ka la la"
slowo = 'la'
policz = tekst.count("la")
policz2 = tekst.count(slowo)
print(policz)
print(policz2)

#Zad.7
a = "To jest łańcuch"
print(a[1],a[-1])

#Zad.8
tekst = "la la baba ka la la"
podziel = tekst.split()
print(podziel)

#Zad.9
str = "Format"
fl = 2.22
print(str, fl)
print(hex(0XFF))
szesnstkowa = 0x1f
print('{0:x}'.format(szesnstkowa))


# ==========================================================================

import sys
import math

ZADANIA DOMOWE LISTA LAB2

#Zad. 1
sporty = ["Rower", "Bieganie", "Pływanie", "Piłka nożna"]
sporty.reverse()
sporty.append("Koszykowka")
sporty.append("Piłka ręczna")
print(sporty)

#Zad. 2
slownik = {"itd." : "i tak dalej",
           "ww." : "wyzej wymienione",
           "ds." : "do spraw"}
print(slownik)


#Zad. 3
slownik2 = {"GTA" : "Grand Theft Auto",
            "exp." : "Experience Points",
            "HP" : "Health Points"}
for a in slownik2:
    print(a)

#Zad. 4
ile=0
zdanie=input("Wpisz zdanie: ")
for x in zdanie:
    if x == 'a':
        ile+=1
print(ile)

# Zad. 5
sys.stdout.write('podaj a: ')
a = sys.stdin.readline()
sys.stdout.write('podaj b: ')
b = sys.stdin.readline()
sys.stdout.write('podaj c: ')
c = sys.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
sys.stdout.write(str(math.pow(a, b) + c))

#Zad. 6
a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
c = float(input("Podaj trzecia liczbe: "))
if (a > b) and (a > c):
    maks = a
elif (b > a) and (b > c):
    maks = b
else:
    maks = c
print("Najwieksza liczba jest ", maks)

# Zad.6   DRUGA WERJSA - LEPSZA
a = input("Wprowadź liczbę a: ")
b = input("Wprowadź liczbę b: ")
c = input("Wprowadź liczbę c: ")

a = int(a)
b = int(b)
c = int(c)
if a == b == c:
    print("wprowadziłeś trzy takie same liczby")
elif a >= b:
    if a > c:
        print("liczba",a,"jest największa")
    else:
        print("liczba",c, "jest największa")
elif b > a:
    if b > c:
        print("liczba",b,"jest największa")
    else:
        print("liczba",c, "jest największa")


#Zad. 7
liczby = [1, 2.2, 3, 4.4, 5, 6.6, 7, 8.8, 9]
#for a in liczby:
liczby2 = [x**2 for x in liczby]
print(liczby2)

#Zad. 8
parzyste = []
x = 0
while x !=10:
    x += 1
    if x%2==0:
        parzyste.append(x)
print(parzyste)


#Zad. 8   - WERSJA ROZBUDOWANA
licznik = 0
liczby_parzyste = []
while licznik < 10:
    try:
        liczba = input('wprowadź liczbę: ')
        if float(liczba):
            liczba = float(liczba)
            if liczba % 2 == 0:
                liczby_parzyste.append(liczba)
                licznik += 1
    except ValueError:
        print('nie wczytano liczby')
print(liczby_parzyste)
print(len(liczby_parzyste))

#Zad. 9
liczba = input("Podaj liczbę nieujemną: ")
liczba = float(liczba)
if liczba>0:
    print(math.sqrt(liczba))
else:
    print("Podana liczbę ujemną")

try:
    print(math.sqrt(liczba))
except : #co tu dac
    print("Podana liczbę ujemną")

# Zad. 9 - Poprawione
a = input('podaj liczbę: ')
try:
    a = int(a)
    pierwiastek = math.sqrt(a)
    print(pierwiastek)
except ValueError:
    if type(a) != int:
        print('nie wczytano liczby')
    elif a < 0:
        print('liczba a nie może być mniejsza od 0')
        
# ==========================================================================

import sys
import math
import random

PRACA DOMOWA LAB3

# #Zad. 1
a = []
for x in range(1,11):
    a.append(1-x)
print(a)

b = []
for y in range(8):
    b.append(4**y)
print(b)

c = []
for z in b:
    if z % 2 == 0:
        c.append(z)
print(c)

#Zad. 1 - SKRÓCONA WERSJA
a = [1-x for x in range(1, 11)]
b = [4**x for x in range(0, 8)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)


#Zad. 2
lista1 = []
i=1
while i<11:
    x = (random.randint(0, 30))
    lista1.append(x)
    i+=1
print(lista1)

lista2 = []
for y in lista1:
    if y % 2 == 0:
        lista2.append(y)
print(lista2)


#Zad. 2 - SKRÓCONA WERSJA
lista1 = []
licznik = 0
while licznik != 10:
    a = random.randint(0, 100)
    lista1.append(a)
    licznik += 1
print(lista1)
nowa_lista = [x for x in lista1 if x % 2 == 0]
print(nowa_lista)


#Zad. 3
slownik = {'szt.' : ["Mango", "Pączek", "Bluza"],
           'litr' : ["Pepsi","Olej"],
           'kg' : ["Mąka","Banany"]}
# print(slownik)
# sztuki = []
# for key in slownik.items():
#     if key == 'szt.'
#         sztuki.append(values)
sztuki =  [slownik[x] for x in slownik.keys() if x=='szt.']
print(sztuki)

#Zad. 3   - SKRÓCONA WERSJA
slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
print(lista)


#Zad. 4
def trojkat_prostokatny(a,b,c):
    wzor = (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)

    if wzor:
        print("Trojkąt jest prostokątny!")
        return 1
    else:
        print("Trojkąt nie jest prostokątny!")
        return 0
print(trojkat_prostokatny(3,4,5))
print(trojkat_prostokatny(5,4,3))
print(trojkat_prostokatny(4,6,8))

#Zad. 5
def pole_trapezu (a,b,h):
    pole = ((a+b)*h)/2
    return pole
print(pole_trapezu(4,6,8))

#Zad. 6
def iloczyn(a=1,b=4,ile=10):
  for i in range (ile):
    a*=b
  return a
print(iloczyn())

# Zad. 6  - DRUGA WERSJA
def iloczyn(a=1, b=4, ile=10):
    licznik = 0
    while licznik != ile:
        a *= b
        licznik += 1
    return a
print(iloczyn())

#Zad. 7
def iloczyn2(*liczby, b):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn_liczb = liczby[0] * b
        for a in range(1, len(liczby), 1):
            iloczyn_liczb *= b
        return iloczyn_liczb
print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))

#Zad. 8
def lista_zakupow(** rzeczy):
    koszt_zakupow = 0
    for koszt in rzeczy:
        koszt_zakupow += rzeczy[koszt]
    return len(rzeczy), round(koszt_zakupow,2)
print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))

#Zad. 9
print(arytmetyczny.n_ty_wyraz(6, 6, 2))
print(arytmetyczny.suma_ciagu(6, 16, 6))
print(geometryczny.n_ty_wyraz(1, 4, 11))

import ciagi.arytmetyczny
from ciagi import

# # Pliki w folderze projektu - Nazwa i pozniej zawartosc

#__init__.py
#__all__ = ['arytmetyczny', 'geometryczny']


#arytmetyczny.py
#def n_ty_wyraz(a1, n, r):
#    return a1 + (n-1)*r

#def suma_ciagu(a1, an, n):
#    return (a1+an)/2*n


#geometryczny.py
# def n_ty_wyraz(a1, q, n):
#     return a1 * q**(n-1)
# 
# def suma(a1, n, q):
#     if q == 1:
#         return a1*n
#     else:
#         return a1 * (1-q**n)/(1-q)

# ==========================================================================

import sys
import math

PRACA DOMOWA LAB4

#Zad.1
liczby=[]
for x in range(0,31):
    liczby.append(x * 2)
file = open("pomnozone.txt", "w+")
file.write(str(liczby))
file.close()

# Zad. 1 - DRUGA WERSJA
a = [x * 2 for x in range(0, 31)]
plik = open('zad1.txt', 'w')
for b in a:
    plik.write(str(b))
    plik.write('\n')
plik.close()
print(a)

#Zad.2
with open('pomnozone.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')

#Zad.2 - DRUGA WERSJA
plik = open('zad1.txt')
zawartosc = plik.readlines()
plik.close()
print(zawartosc)

#Zad.3
print("Wpisz kilka linijek tekstu")
linijki = sys.stdin.readline()
plik = open('linijki.txt', 'w+')
plik.write(linijki)
plik.close()
with open('linijki.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')

#Zad.3 - DRUGA WERSJA - JAK TO NAPRAWIC?
with open('zad3.txt', 'a+') as plik:
    for b in a:
        plik.write(str(b))
        plik.write('\n')
with open('zad3.txt', 'r') as plik:
    for a in plik:
        print(a)


#Zad.4
class NaZakupy():
    """Zakupy"""
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
            self.nazwa_produktu = nazwa_produktu
            self.ilosc = ilosc
            self.jednostka_miary = jednostka_miary
            self.cena_jed  = cena_jed
   def wyswietl_produkt(self):
        print("{}, {}{} w cenie {} zł za {}" .format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed, self.jednostka_miary))
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
    def ile_kosztuje(self):
        kwota = self.cena_jed * self.ilosc
        print(kwota)

zakup = NaZakupy("Ziemniaki",3,"kg",2)
#zakup.wyswietl_produkt()   #dlaczego wyrzuca błąd?
zakup.ile_produktu()
zakup.ile_kosztuje()


#Zad. 5 - DRUGA WERSJA
class NaZakupy():
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("{}, {} {} w cenie {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))

    def ile_produktu(self):
        print("{} {}".format(self.ilosc, self.jednostka_miary))

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed


mleko = NaZakupy('mleko', 2, 'sztuki', 2.50)
mleko.wyswietl_produkt()
mleko.ile_produktu()
print(mleko.ile_kosztuje())


Zad.5
class CiagArytmetyczny:
    def __init__(self):
        self.a1 = None
        self.r = None
        self.n = None
        self.ciag = []

    def wyswietl_dane(self):
        for element in self.ciag:
            print(element)

    def pobierz_elementy(self):
        while True:
            wejscie = input("Podaj liczbę lub wpisz 'koniec'\n")
            if wejscie != 'koniec':
                self.ciag.append(int(wejscie))
            else:
                break

    def pobierz_parametry(self):
        self.a1 = int(input("Podaj pierwszy wyraz ciągu: "))
        self.r = int(input('Podaj różnicę ciągu arytmetycznego: '))
        self.n = int(input('Podaj ilość wyrazów ciągu arytmetycznego: '))

    def policz_sume(self):
        return sum(self.ciag)

    def policz_elementy(self):
        if (self.a1 is not None) & (self.r is not None) & (self.n is not None):
            licznik = 0
            suma = self.a1
            while licznik != self.n:
                self.ciag.append(suma)
                suma += self.r
                licznik += 1



ciag2 = CiagArytmetyczny()
ciag2.wyswietl_dane()
ciag2.pobierz_parametry()
ciag2.policz_elementy()
ciag2.wyswietl_dane()


#Zad. 6
class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += (ile_krokow * self.krok)
    def idz_w_dol(self, ile_krokow):
        self.y -= (ile_krokow * self.krok)
    def idz_w_prawo(self, ile_krokow):
        self.x += (ile_krokow * self.krok)
    def idz_w_lewo(self, ile_krokow):
        self.y -= (ile_krokow * self.krok)

    def pokaz_gdzie_jestes(self):
        print("Robaczek znajduje się na współrzędnych x = " + str(self.x) + " i y =" + str(self.y))

ruch = Robaczek(0, 0, 1) #pozycja startowa i wielkosc kroku robaczka

ruch.idz_w_prawo(3)
ruch.idz_w_lewo(7)
ruch.idz_w_gore(1)
ruch.idz_w_dol(2)
ruch.pokaz_gdzie_jestes()
