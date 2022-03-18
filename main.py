# # # # # # # a = []
# # # # # # # for x in range(0, 10):
# # # # # # #     a.append(x**2)
# # # # # # # print(a)
# # # # # # # a2 = [x**2 for x in range(0, 10)]
# # # # # # # print(a2)
# # # # # # # b = []
# # # # # # # for x in range(0,5):
# # # # # # #     b.append(3**x)
# # # # # # # print(b)
# # # # # # # b2 = [3**x for x in range(0,6)]
# # # # # # #
# # # # # # # c = []
# # # # # # # for x in a:
# # # # # # #     if x%2 == 1:
# # # # # # #         c.append(x)
# # # # # # # print(c)
# # # # # # # c2 = [x for x in a if x%2 == 1]
# # # # # # #
# # # # # # # lista = []
# # # # # # #
# # # # # # # for a in [1, 2, 3]:
# # # # # # #     for b in [4, 5, 6]:
# # # # # # #         lista.append((a,b))
# # # # # # # lista2 = [(a,b) for a in [1, 2, 3] for b in [4, 5, 6]]
# # # # # # # print(lista)
# # # # # # # print(lista2)
# # # # # #
# # # # # # slownik = {'PZU': 'Państwowy zakład ubezpieczeń',
# # # # # #            'ZUS': 'Zakład ubezpieczeń zdrowotnych',
# # # # # #            'PKO': 'Państwowa kasa oszczędności'}
# # # # # # slownik2 = {}
# # # # # # print(slownik)
# # # # # # for key, value in slownik.items():
# # # # # #     slownik2[value] = key
# # # # # # print(slownik2)
# # # # # # slownik3 = {value: key for key, value in slownik.items()}
# # # # # # print(slownik3)
# # # # #
# # # # # import math
# # # # # def rownanie_kwadratowe(a, b ,c):
# # # # #     delta = b**2 - 4 * a * c
# # # # #     if delta < 0:
# # # # #         print('brak rozwiazan')
# # # # #         return -1
# # # # #     elif delta == 0:
# # # # #         print('jedno rozwiazanie')
# # # # #         x = (-b)/(2*a)
# # # # #         return x
# # # # #     else:
# # # # #         print('dwa rozwiazania')
# # # # #         x1 = ((-b) - math.sqrt(delta))/(a*2)
# # # # #         x2 = ((-b) - math.sqrt(delta))/(a*2)
# # # # #         return x1, x2
# # # # #
# # # # # print(rownanie_kwadratowe(6,1,3))
# # # # # print(rownanie_kwadratowe(1,2,1))
# # # # # print(rownanie_kwadratowe(1,4,1))
# # # # #
# # # # #
# # # #
# # # #
# # # # def podzielna(x):
# # # #     if x % 5 == 0:
# # # #         print('Jest podzielna przez 5')
# # # #     else:
# # # #         print('Nie jest podzielna przez 5')
# # # #
# # # # podzielna(5)
# # # import math
# # #
# # #
# # # def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
# # #     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# # #
# # #
# # # print(dlugosc_odcinka())
# # #
# # # print(dlugosc_odcinka(2, 2, y2=5, x2=4))
# # #
# # # print(dlugosc_odcinka(y2=3, x2=7))
# #
# # def ciag(* liczby):
# #     if len(liczby) == 0:
# #         return 0
# #     else:
# #         suma = 0
# #         for i in liczby:
# #             suma += i
# #             return suma
# #
# # print(ciag())
# #
# # print(ciag(1, 2.5, 3, 4, 6, 5, 9))
#
# def gwiazdki(** rzeczy):
#     for cos in rzeczy:
#         print(cos)
#         print(rzeczy[cos])
#
# gwiazdki(gry=['planszówki','komputerowe'], a=5)
#
#
# from cwicz import *
# napis = 'dzis jest piatek jade na kaszuby'
# test.wyswietl(napis)
#
# odcinek = 5
#
# test.dlugosc(napis)
#
#
#
# print(dodawanie.dodaj(5,5))
#
#


A = []
for x in range(1, 10):
    A.append(1-x)
print(A)

B = []
for x in range(1,7):
    B.append(4**x)
print(B)

C = []
for x in B:
    if x%2 == 0:
        C.append(x)
print(C)


lista1 =[]
lista2 = []
for a in [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10]:
    lista1.append(a)
for x in lista1:
        if x%2==0:
            lista2.append(x)

print(lista1)
print(lista2)

zakupy = {'chleb' : 'sztuka', 'Mleko' : 'sztuka', 'Ziemniaki' : 'kilogramy', 'Woda' : 'litry'}