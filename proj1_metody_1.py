# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:17:48 2019

@author: Paulina
"""

import matplotlib.pyplot as plt

xa='1186.00'   
ya='17962.69'
xb='1144.74'   
yb='180.22'
xc='1184.31'   
yc='18.14'
xd='11.14'  
yd='179.41'

#sprawdzenie czy wprowadzone wartosci są danymi liczbowymi

wsp=[xa,ya,xb,yb,xc,yc,xd,yd] #lista ze współrzędnymi
for element in wsp:
    if element.replace('.','').isdigit():
        T=element.replace('.','').isdigit() #sprawdzenie czy wartosci są
                                            #wartosciami liczbowymi
xa=float(xa) #zamiana wartosci ze stringow na floaty
xb=float(xb)
xc=float(xc)
xd=float(xd)
ya=float(ya)
yb=float(yb)
yc=float(yc)
yd=float(yd)
       
#policzenie delt        
dxab=xb-xa
dyab=yb-ya
dxcd=xd-xc
dycd=yd-yc
dxac=xc-xa
dyac=yc-ya
   

if dxab*dycd-dyab*dxcd!=0 and dxab*dycd-dyab*dxcd!=0: #upewnienie sie ze mianownik nie jest 0
    #wyliczenie parametrów t
    t1=(dxac*dycd-dyac*dxcd)/(dxab*dycd-dyab*dxcd)
    t2=(dxac*dyab-dyac*dxab)/(dxab*dycd-dyab*dxcd)

  
if (0<=t1<=1) and (0<=t2<=1):
    rozw=print("Punkt przecięcia jest wspólny dla obu odcinków")
    #współrzędne punktu przecięcia odcinka    
    xp=round(xa+t1*dxab,3)
    yp=round(ya+t1*dyab,3)
elif (0<=t1<=1) and ((0>t2) or (t2>1)):
    rozw=print("Punkt przecięcia leży na przedłużeniu odcinka")
    xp=round(xa+t1*dxab,3)
    yp=round(ya+t1*dyab,3)
elif ((0>t1) or (t1>1)) and (0<=t2<=1):
    rozw=print("Punkt przecięcia leży na przedłużeniu odcinka")
    xp=round(xa+t1*dxab,3)
    yp=round(ya+t1*dyab,3)
else:
    rozw=print("Punkt przecięcia leży na przedłużeniu obu odcinków")
    xp=round(xa+t1*dxab,3)
    yp=round(ya+t1*dyab,3)
    
    
#funkcja sprawdzająca polozenie punktu P względem odcinka AB
def polozenie_ab(xa,ya,xb,yb,xp,yp): 
  det_abp=xa*yb+xb*yp+xp*ya-xp*yb-xa*yp-xb*ya   
  if det_abp>0:
     or_ab='punkt P leży po prawej stronie odcinka AB'
  elif det_abp<0:
     or_ab='punkt P leży po lewej stronie odcinka AB'
  elif det_abp==0:
     or_ab='punkty P,A,B są współliniowe'
     
  or_ab_ost=str(or_ab)
     
  return or_ab_ost

    
#funkcja sprawdzająca polozenie punktu P względem odcinka CD    
def polozenie_cd(xc,yc,xd,yd,xp,yp):
  det_cdp=xc*yd+xd*yp+xp*yc-xp*yd-xc*yp-xd*yc
  if det_cdp>0:
     or_cd='punkt P leży po prawej stronie odcinka CD'
  elif det_cdp<0:
     or_cd='punkt P leży po lewej stronie odcinka CD'
  elif det_cdp==0:
     or_cd='punkty P,C,D są współliniowe'
      
  or_cd_ost=str(or_cd)
  
  return or_cd_ost
    

#funkcja generująca wykres
def wykres(xa,ya,xb,yb,xc,yc,xd,yd,xp,yp,kolor1,kolor2):
  let = ["A","B","C","D","P"]
  X1=[xa,xb,xc,xd,xp]
  Y1=[ya,yb,yc,yd,yp]
  ax1=plt.subplot()
  ax1.scatter(X1,Y1)
  ax1.plot([xa,xb],[ya,yb], color=kolor1)
  ax1.plot([xc,xd],[yc,yd], color=kolor2)
  ax1.plot([xa,xp],[ya,yp], linestyle="--", color=kolor1)
  ax1.plot([xd,xp],[yd,yp], linestyle="--", color=kolor2)
  ax1.set_xlabel('X')
  ax1.set_ylabel('Y')
    
  for (x,y,l) in zip(X1,Y1,enumerate(let)):
    ax1.annotate("{}({};{})".format(l[1],x,y),xy=(x,y))
    plt.show()
         
  return (plt)


    




    
    
    









