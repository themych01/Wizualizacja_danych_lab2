# plik=open("tekst","r")
# znaki = plik.read(10)
# linia = plik.readline()
# wiersze = plik.readlines()
# plik.close()
# print(znaki)
# print("\n")
# print(linia)
# print("\n")
# print(wiersze)
#
# import sys
# print("Podaj kierunek studiów, rok i specjalność")
# dane = sys.stdin.readline()
# plik = open("dane.txt","w+")
# plik.write(dane)
# plik.close()
#
# lista = []
#
# for x in range(6):
#     lista += [x]
# plik = open("dane.txt","a+")
# plik.writelines(str(lista))
#
# with open("tekst","r") as plik:
#     for linia in plik:
#         print(linia,end="")
#
#

# class PierwszaKlasa:
#     """Pierwsza klasa Python"""
#     atrybut = 54321
#     def pierwsza_metoda(self):
#         return "teraz działa pierwsza Metoda"
# obiekt = PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# print(obiekt.pierwsza_metoda())
#
# obiekt.tekst = "la la la"
# print(obiekt.tekst)
# nowy_obiekt = PierwszaKlasa()
# print(nowy_obiekt.tekst)
#
# class Ksztalty:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.opis = "To bedzie klasa dla ogolnych ksztaltow"
#     def pole(self):
#         return self.x * self.y
#     def obwod(self):
#         return 2* self.x + 2* self.y
#     def dodaj_opis(self, text):
#         self.opis = text
#     def skalowaniee(self,czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
# prostokat= Ksztalty(10,30)
#
# print(prostokat.pole())
# print(prostokat.obwod())
# prostokat.dodaj_opis("Prostokat")
# print(prostokat.opis)
# prostokat.skalowaniee(0.5)
# print(prostokat.x)
# print(prostokat.y)
# zad1
# a = [ x * 2 for x in range (0,31)]
# plik = open("wynik", 'w+')
#
# for b in a:
#     plik.write(str(b))
#     plik.write('\n')
# plik.close()
# print(a)
#  zad2
# plik = open('wynik','r')
# tresc = plik.readlines()
# plik.close()
# print(tresc)
# zad3
# with open('zad3.txt', 'w') as plik:
#     for x in range(1,5):
#         plik.write(str(x))
#         plik.write('\n')
# with open('zad3.txt','r') as plik:
#     for a in plik:
#         print(a)

# 5. (7.pkt) Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby całkowite a i b.
# Zadaniem jest wykonanie działania ab i zapisanie wyniku do pliku o nazwie zadanie5.txt.
# W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, do tego celu użyj składni try-except.

# # Zad5
# print("Podaj dwie liczby całkowite: ")
#
# try:
#     a = input("Podaj Liczbę a: ")
#     b = input("Podaj Liczbę b: ")
#     a = int(a)
#     b = int(b)
#     print(pow(a, b))
#     plik = open('zad5.txt', 'w+')
#     plik.writelines(str(pow(a, b)))
# except ValueError:
#     print("Podano złe dane.")
# except TypeError:
#     print("Poproszę liczby całkowite.")

# 4. (2pkt.) Napisz skrypt, który policzy i wyświetli następujące wyrażenie:
# 𝜋3+ √𝑙𝑜𝑔264+sin (45)4
# Wynik zaokrągli do dwóch miejsc po przecinku.

# Zad4
#
# import math
# import sys as system
#
# pi = math.tau
#
# print(round(pow(pi,3) + (pow(math.log(2,64)+math.sin(45),-4)),2))

# 3. (5pkt.) Napisz skrypt, w którym utworzysz listę z liczbami całkowitymi, a następnie za pomocą python comprehension utwórz nową listę,
# która będzie zawierała co drugi element z pierwszej listy, na koniec wyświetl obydwie listy.
#
# lista = [3, 2, 5, 6, 7, 8, 9, 10]
# lista2 = []
# lista2 =[i for i in lista if lista.index(i) %2 !=0 ]
# print(lista2)
# lista2 = [(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(lista2)


# skroty = {"PZU": "Państwowy zakład ubezpieczeń",
#  "ZUS": "Zaklad ubezpieczeń społecznych",
#  "PKO": "Państwowa kasa oszczędności"}
# odwrocone = {}
# for key,value in skroty.items():
#  odwrocone[value] = key
# print(odwrocone)
# #wersja z python comprehension
# odwrocone2 = {value: key for key, value in skroty.items()}
# print(odwrocone2)
# print(skroty)
# # licznik = 1
# for x in lista:
#     if licznik <= len(lista):
#         x = lista[licznik]
#         lista2.append(x)
#     else:
#         break
#     licznik += 2
#
# print(lista)
# print(lista2)
#
# lista = [3, 2, 5, 6, 7, 8, 9, 10]
# licznik = 1
# lista2 = []
# while licznik != len(lista):
#     x = lista[licznik]
#     lista2.append(x)
#     licznik += 2
#
# print(licznik)
# print(lista2)

# 1. (6pkt.) Napisz funkcje, która jako argument przyjmuje słownik gdzie klucz i wartość będą dowolnego typu.
# Funkcja ma za zadanie stworzyć i zwrócić listę, do której trafią tylko kluczę ze słownika, które będą miały wartość jako liczbę całkowitą.


# def slownik():
#     lista = []
#     slowniki = {'1': '45', '2': '87'}
#     l = 0
#     k = len(slowniki.keys())
#     for x in slowniki:
#         if l != k:
#             try:
#                 lista.append(slowniki.get(x))
#                 l += 1
#             except TypeError:
#                 "to nie jest calkowita"
#         else:
#             print(lista)
#             break
#
#
# print(slownik())

# 1. (6pkt.) Napisz funkcje, która jako argument przyjmuje słownik gdzie klucz i wartość będą dowolnego typu.
# Funkcja ma za zadanie stworzyć i zwrócić listę, do której trafią tylko kluczę ze słownika, które będą miały wartość jako liczbę całkowitą.

# 3. (5pkt.) Napisz skrypt, w którym utworzysz listę z liczbami całkowitymi, a następnie za pomocą python comprehension utwórz nową listę,
# która będzie zawierała co drugi element z pierwszej listy, na koniec wyświetl obydwie listy.

# 5. (7.pkt) Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby całkowite a i b.
# Zadaniem jest wykonanie działania ab i zapisanie wyniku do pliku o nazwie zadanie5.txt.
# W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, do tego celu użyj składni try-except.

def to_lubie(** rzeczy):
 for cos in rzeczy:
     print("To jest ")
     print(cos)
     print(" co lubie ")
     print(rzeczy[cos])
to_lubie(slodycze="czekolada", rozrywka=['gry', 'filmy'])