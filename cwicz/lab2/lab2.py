# lista= ['wyraz',4.23,5.6,2,10,[4,5,6]]
# lista.append('slow')
# lista.append(5.75)
# print(lista)
# lista.insert(1,'pierwszy')
# lista.insert(7,3)
# print(lista)
#
# lista.pop()
# print(lista)
#
# lista.pop(2)
# print(lista)
#
# lista.remove('pierwszy')
# print(lista)
#
# del lista[5]
# print(lista)
#
# lista.extend(((2,2,'n')))
# print(lista)
#
# lista.reverse()
# print(lista)
#
# nowa_lista=[7,6,8.2,1,2.2,1.1,10,6,3]
# nowa_lista.sort()
# print(nowa_lista)
#
# slownik = {1:22, 2:22, 3:33, 4.5:10, "cos":"ktos",4.6:'wartosci'}
# slownik['klucz']='wartosc'
# slownik['6']=1.1
# print(slownik)
#
# print(slownik[4.5])
#
# slownik.pop(4.5)
# print(slownik)
#
# print(slownik.keys())
#
# print(slownik.values())
#
# del slownik[1]
#
# print(slownik)
#
# napis=input("wpisz dowolny komunikat: ")
# print(napis)
#
# print(type(napis))
#
# liczba = input("wpisz dowolna liczbe: ")
# print(liczba)
# print(type(liczba))
#
# liczba = int(liczba)
# print(type(liczba))
#
#
# liczba=float(liczba)
# print(liczba)
#
# print(type(liczba))


import sys as system

# system.stdout.write("wpisz komunikat: ")
# napis = system.stdin.readline()
# system.stdout.write((napis))

# lista = ['a',5,6,7.5]
# for x in lista:
#     print(x)

# z=0
#
# while z !=10:
#     print(z)
#     z += 1
# else:
#     print("Wyświetlonych zostało " +str(z) + " liczb")

# lista = [4,6,2,3,5,9,1]
# lista2 = [7,3,4,6]
# suma = []
#
# for a in lista:
#     for b in lista2:
#         wynik = a+b
#         suma.append(wynik)
#     print(suma)

# print("Prosze podac pierwsza liczbe")
# licz1=input()
#
# print('Prosze podac druga liczba')
# licz2=input()
#
# try:
#     wynik = int(licz1)/int(licz2)
#     print("wynik= " + str(wynik))
# except ZeroDivisionError:
#     print("Tylko Chuck Norris może dzielić przez zero!")

# ZAD1
# lista = []
# lista.append('Koszykówka')
# lista.append('Siatkówka')
# lista.append('Squash')
# lista.append('Ping Pong')
# print(lista)
# lista.reverse()
# lista.insert(4,'Pilka nozna')
# print(lista)
#

# # Zad2
# slownik={'ASAP':'As soon as possible','DIY':'Do it Yourself','FYI':'For your information'}
# print(slownik)
#
# zad3
# slownik_gier = {"RPG":"Baldur's Gate 1&2","FPS-RPG":"Metro Exodus","FPS":"Counter-Strike"}
#
# print(slownik_gier)
#
# x = len(slownik_gier)
# print(x)
#
# zad4
#
# print("Odpisz pelnym zdaniem. \n Jak Masz na Imię? ")
# zdanie = input()
# print(zdanie.count('a'))
# # zad 5
#
# import sys as system
#
# system.stdout.write("Podaj 3 liczby: ")
# a = system.stdin.readline()
# b = system.stdin.readline()
# c = system.stdin.readline()
#
# wynik = pow(int(a),int(b))+int(c)
# wynik=str(wynik)
# system.stdout.write("Wynikiem jest:" + str(wynik))


# # zad6
# print("Podaj trzy liczby calkowite:")
# a = input("Wprowadz liczbe a: ")
# b = input("Wprowadz liczbe b: ")
# c = input("Wprowadz liczbe c: ")
# a = int(a)
# b = int(b)
# c = int(c)
#
# if a == b == c:
#     print("Wprowadziles 3trzy takie same liczby!")
# elif a >= b:
#     if a>c :
#         print("liczba ",a," jest najwieksza")
#     else:
#         print("liczba ",c, " jest najwieksza")
# elif b>a :
#     if b > c :
#         print("liczba ",b," jest najwieksza")
#     else:
#         print("liczba ",c," jest najwieksza")
#
# zad 7
# lista = [4,5,2.5,3.3]
#
# for x in lista:
#     x = x**2
#     print(x)
#

# # zad 8
# lista=[]
# z=1
# while z!=10:
#     print("Podaj liczbe: ")
#     liczba = input()
#     z+=1
#     if int(liczba) %2 == 0:
#         lista.append(liczba)
#
#
# print(lista)
# # zad9
# import math
# print("Podaj liczbe : ")
# a=input()
# try:
#     a=int(a)
#     a = math.sqrt(a)
#     print(a)
# except ValueError:
#     if type(a) != int:
#         print('nie wczytano liczby')
#     elif a<0 :
#         print('liczba a nie moze byc mniejsza od 0')