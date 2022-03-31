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

