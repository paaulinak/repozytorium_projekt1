# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:46:02 2019

@author: Paulina
"""

import tkinter as tk 
import matplotlib.pyplot as plt
import numpy as np
from proj1_metody_1 import wykres
from proj1_metody_1 import polozenie_ab
from proj1_metody_1 import polozenie_cd


def dodaj_okno1(okno_rodzic1,pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10):
  okno1=tk.Toplevel(okno_rodzic1) #dodanie nowych okien dla odpowiednich wartosci
  okno1.title('wynik')

  xa_st=str(pole1.get()) #pobieranie danych od użytkownika
  ya_st=str(pole2.get())
  xb_st=str(pole3.get())
  yb_st=str(pole4.get())
  xc_st=str(pole5.get())
  yc_st=str(pole6.get())
  xd_st=str(pole7.get())
  yd_st=str(pole8.get())
  kolor1=str(pole9.get())
  kolor2=str(pole10.get())
    
  wsp=[xa_st,ya_st,xb_st,yb_st,xc_st,yc_st,xd_st,yd_st]
  for element in wsp: #sprawdzenie czy podane dane są wartosciami liczbowymi
    if element.replace('.','').isdigit():
        T=element.replace('.','').isdigit()
        
  xa=float(xa_st)
  xb=float(xb_st)
  xc=float(xc_st)
  xd=float(xd_st)
  ya=float(ya_st)
  yb=float(yb_st)
  yc=float(yc_st)
  yd=float(yd_st)
       
  #policzenie delt        
  dxab=xb-xa
  dyab=yb-ya
  dxcd=xd-xc
  dycd=yd-yc
  dxac=xc-xa
  dyac=yc-ya
   
  #wyliczenie parametrów t
  #upewniam sie ze mianownik nie jest 0
  if dxab*dycd-dyab*dxcd!=0 and dxab*dycd-dyab*dxcd!=0:
     t1=(dxac*dycd-dyac*dxcd)/(dxab*dycd-dyab*dxcd)
     t2=(dxac*dyab-dyac*dxab)/(dxab*dycd-dyab*dxcd)  
  if (0<=t1<=1) and (0<=t2<=1):
      rozw="Punkt przecięcia jest wspólny dla obu odcinków"
     #współrzędne punktu przecięcia odcinka    
      xp=round(xa+t1*dxab,3)
      yp=round(ya+t1*dyab,3)
  elif (0<=t1<=1) and ((0>t2) or (t2>1)):
      rozw="Punkt przecięcia leży na przedłużeniu odcinka"
      xp=round(xa+t1*dxab,3)
      yp=round(ya+t1*dyab,3)
  elif ((0>t1) or (t1>1)) and (0<=t2<=1):
      rozw="Punkt przecięcia leży na przedłużeniu odcinka"
      xp=round(xa+t1*dxab,3)
      yp=round(ya+t1*dyab,3)
  else:
      rozw="Punkt przecięcia leży na przedłużeniu obu odcinków"
      xp=round(xa+t1*dxab,3)
      yp=round(ya+t1*dyab,3)
   
  xp_wynik=str(xp)
  yp_wynik=str(yp)
  
  
  rozw_ost=str(rozw)
  
  xp=float(xp)
  yp=float(yp)

  or_ab_ost=polozenie_ab(xa,ya,xb,yb,xp,yp)
  or_cd_ost=polozenie_cd(xc,yc,xd,yd,xp,yp)
  
       
  tk.Label(okno1, text='orientacja punktu P:  '+rozw_ost).pack()
  tk.Label(okno1, text='współrzędna X punktu przecięcia P:  '+xp_wynik).pack()
  tk.Label(okno1, text='współrzędna Y punktu przecięcia P:  '+yp_wynik).pack()
  tk.Label(okno1, text='położenie punktu P względem odcinka AB:  '+or_ab_ost).pack()
  tk.Label(okno1, text='położenie punktu P względem odcinka CD:  '+or_cd_ost).pack()
  tk.Button(okno1, text="generuj wykres",width=15,font=("Helvetica", 12),
            command=lambda:wykres(xa,ya,xb,yb,xc,yc,xd,yd,xp,yp,kolor1,kolor2)).pack()
   

  #zapis wyników obliczeń do pliku 
  let = ["A","B","C","D","P"]
  X1=[xa,xb,xc,xd,xp]
  Y1=[ya,yb,yc,yd,yp]
  zap=open('proj1_wyniki.txt','w+')
  zap.write(34*'-')
  zap.write("\n|{:^10}|{:^10}|{:^10}|\n".format('punkt','X [m]','Y [m]'))
  zap.write(34*'-')
  for(l,x,y) in zip(let,X1,Y1):
      x1=round(x,3)
      y1=round(y,3)
      zap.write("\n|{:^10}|{:^10}|{:^10}|\n".format(l,x1,y1))
  #zap.write("\n")
  zap.write(34*'-')
  zap.close()
 

#funkcja czyszcząca wypełnione pola    
def clear(pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10):
    pole1.delete(0, 'end')
    pole2.delete(0, 'end')
    pole3.delete(0, 'end')
    pole4.delete(0, 'end')
    pole5.delete(0, 'end')
    pole6.delete(0, 'end')
    pole7.delete(0, 'end')
    pole8.delete(0, 'end')
    pole9.delete(0, 'end')
    pole10.delete(0, 'end')
    

root = tk.Tk() # otworzenie głównego okna

l1 = tk.Label(root, text="wpisz współrzędne",font=("Arial", 12)) #przypisanie własciwosci do stworzonych okien 
l2 = tk.Label(root,text="Dla punktu A:  ", width=15)
l3 = tk.Label(root,text="XA [m]: ", width=15)
e1 = tk.Entry(root, width = 15)
l4 = tk.Label(root, text="YA [m]: ",width=15)
e2 = tk.Entry(root, width = 15)
l5 = tk.Label(root, text="Dla punktu B: ", width=15)
l6 = tk.Label(root, text="XB [m]: ",width=15)
e3 = tk.Entry(root, width = 15)
l7 = tk.Label(root, text="YB [m]: ",width=15)
e4 = tk.Entry(root, width = 15)
l8 = tk.Label(root, text="Dla punktu C: ", width=15)
l9 = tk.Label(root, text="XC [m]: ", width=15)
e5 = tk.Entry(root, width = 15)
l10 = tk.Label(root, text="YC [m]: ", width=15)
e6 = tk.Entry(root, width = 15)
l11 = tk.Label(root, text="Dla punktu D: ", width=15)
l12 = tk.Label(root, text="XD [m]: ", width=15)
e7 = tk.Entry(root, width = 15)
l13 = tk.Label(root, text="YD [m]: ", width=15)
e8 = tk.Entry(root, width = 15)

#dostępne kolory wykresu
n1=tk.Label(root, text="wybierz kolor wykresu",  font=("Arial", 12), width=35)
k1=tk.Label(root, text=" wpisz b", bg="blue", fg="white", width=15 )
k2=tk.Label(root, text=" wpisz g", bg="green", fg="black",width=15 )
k3=tk.Label(root, text=" wpisz r", bg="red", fg="black", width=15 )
k4=tk.Label(root, text=" wpisz c", bg="cyan", fg="black" , width=15)
k5=tk.Label(root, text=" wpisz m", bg="magenta", fg="black", width=15 )
k6=tk.Label(root, text=" wpisz y", bg="yellow", fg="black", width=15)
k7=tk.Label(root, text=" wpisz k", bg="black", fg="white", width=15 )
k8=tk.Label(root, text="wpisz w", bg="white", fg="black" , width=15)


l14=tk.Label(root,width=15, text="wpisz kolor 1: ")
e9=tk.Entry(root, width=15)
l15=tk.Label(root,width=15, text="wpisz kolor 2: ")
e10=tk.Entry(root, width=15)

#dodanie przycisku 'przelicz', który będzie realizował polecenia dla pierwszego okna
b1 = tk.Button(root, text="przelicz",width=15,font=("Helvetica", 12),
               command =lambda:dodaj_okno1(root,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10))
#dodanie przycisku zamykajacego okno
b2   = tk.Button(master=root, text='Quit', width=15,
                    font=("Arial", 12), command=root.destroy)
#dodanie przycisku ktory czysci wartosci
b3=tk.Button(root,width=15,font=("Arial", 12), text="wyczysc", command=lambda:clear(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10))

 

#umiejscowienie elementóW w odpowiednim wierszu (row) i kolumn (column)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
e1.grid(row=2, column=1)
l4.grid(row=2, column=2)
e2.grid(row=2, column=3)
l5.grid(row=3, column=0)
l6.grid(row=4, column=0)
e3.grid(row=4, column=1)
l7.grid(row=4, column=2)
e4.grid(row=4, column=3)
l8.grid(row=5, column=0)
l9.grid(row=6, column=0)
e5.grid(row=6, column=1)
l10.grid(row=6, column=2)
e6.grid(row=6, column=3)
l11.grid(row=7, column=0)
l12.grid(row=8, column=0)
e7.grid(row=8, column=1)
l13.grid(row=8, column=2)
e8.grid(row=8, column=3)

n1.grid(row=0,column=4)
k1.grid(row=1,column=4)
k2.grid(row=2,column=4)
k3.grid(row=3,column=4)
k4.grid(row=4,column=4)
k5.grid(row=5,column=4)
k6.grid(row=6,column=4)
k7.grid(row=7,column=4)
k8.grid(row=8,column=4)

l14.grid(row=9,column=1) #wpisz kolor 1
e9.grid(row=9,column=2) #get kolor1
l15.grid(row=10,column=1) #wpisz kolor 2
e10.grid(row=10,column=2) #get kolor2


b1.grid(row=16, column=0) #przelicz
b2.grid(row=16, column=1) #zamknij
b3.grid(row=16,column=2)


root.mainloop() #to polecenie uruchamia program


  
  
  
  
    
      
    

