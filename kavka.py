import stavitelka as st
import random as rnd
from math import sin, cos, pi

XCOR = 1                    # pocatecni souradnice x (levy dolni roh hradu)
YCOR = 0                    # pocatecni souradnice y (levy dolni roh hradu)
ZCOR = 1                    # pocatecni souradnice z (levy dolni roh hradu)
SIZE = 30                   # pudorysne rozmery hradu
HGHT = 10                   # vyska sten hradu
HGHT_CIMB = 40              # vyska cimburi (kostky v cimburi maji ctvrtinove rozmery -> pro HGHT_CIMB = 40 bude realna vyska 10)
DIAM = 2                    # prumer cimburi
RESOLUTION = int(DIAM*27)   # rozliseni/pocet sloupcu v kruhu (vyssi cislo = vice detailu, vice narocne); vhodny 27nasobek prumeru


def ctverec(xcor: float, ycor: float, zcor: float, size: int, holes: bool = False) -> None:
  '''
  Vykresli ctverec z kostek

  Args:
    xcor (float): x-ova souradnice leveho dolniho rohu (jihozapadni roh)
    ycor (float): y-ova souradnice leveho dolniho rohu (jihozapadni roh)
    zcor (float): z-ova souradnice leveho dolniho rohu (jihozapadni roh)
    size (int): delka steny ctverce
    holes (bool): urcuje, zdali bude kazda druha kostka ve stene ctverce vynechana (stylem hradeb)
  '''

  xdir = True # urcuje jestli stavi stenu v x-ovem smeru
  zdir = not xdir # urcuje jestli stavi stenu v z-ovem smeru

  for _ in range(2): # prvni cyklus - stavba stran jih, sever; druhy cyklus - stavba stran zapad, vychod)
    for j in range(2): # urcuje, kterou stranu z dvojic (jih, sever), (zapad, vychod) zrovna stavim (0 = prvni clen dvojice, 1 = druhy clen dvojice)
      for col in range(size): # kazdy cyklus posune sloupec, ve kterem se stavi, o jedna

        # dela diry ve stene stylem hradeb; bere v uvahu pripad sudych i lichych rozmeru stran
        if (holes) and (col%2 == 1) and (size%2 == 1):
          continue
        elif (holes) and (col%2 == 0) and (size%2 == 0) and (j == 1):
          continue
        elif (holes) and (col%2 == 1) and (size%2 == 0) and (j == 0):
          continue

        barva = ( rnd.random() , 1 , rnd.random() ) # vybere nahodnou barvu kazde kostce
        st.Hranol(x= xcor+(col*xdir)+((j*(size-1))*zdir),
                  y= ycor,
                  z= zcor+((j*(size-1))*xdir)+(col*zdir),
                  barva= barva)

    # prohozeni smeru z x-oveho na z-ovy
    xdir = False
    zdir = not xdir


def kruh(xcor: float, ycor: float, zcor: float, resolution: int, diam: int, holes: bool = False):
  '''
  Postavi kruh

  Args:
    xcor (float): x-ova souradnice kostky, ktera lezi na kruznici uplne vlevo (kostka je levym prusecikem teto kruznice a primky, ktera prochazi stredem kruznice a je rovnobezna s osou x)
    ycor (float): y-ova souradnice kostky, ktera lezi na kruznici uplne vlevo (kostka je levym prusecikem teto kruznice a primky, ktera prochazi stredem kruznice a je rovnobezna s osou x)
    zcor (float): z-ova souradnice kostky, ktera lezi na kruznici uplne vlevo (kostka je levym prusecikem teto kruznice a primky, ktera prochazi stredem kruznice a je rovnobezna s osou x)
    resolution (int): pocet kostek, z kterych je kruh vytvoren (vyssi cislo -> vice vypada jak kruznice/kruh)
    diam (int): prumer kruznice
    holes (bool): urcuje, zdali udela diry v kruznici ve stylu hradeb
  '''
  for i in range(resolution):
    
    # vynechava kazdy druhy sloupec stylem hradeb
    if (holes) and (i%2 == 0):
      continue

    barva = ( rnd.random() , rnd.random() , 1 )

    # koeficient 0.25 -> ponechani rozliseni kruhu - objekt vypada vice jako kruh i pri mensich prumerech
    st.Hranol(x= xcor+(diam+0.25)*sin((i*(360/resolution))*(pi/180)),
              y= ycor*0.25,
              z= zcor+(diam+0.25)*cos(i*(360/resolution)*(pi/180)),
              sx= 0.25,
              sy= 0.25,
              sz= 0.25,
              ry= i*(360/resolution),
              barva= barva)


def vez(xcor: float, ycor: float, zcor: float, height: int, size: int) -> None:
  '''
  Postavi vez ze ctvercu naskladanych na sebe

  Args:
    xcor (float): x-ova souradnice leveho dolniho rohu (jihozapadni roh)
    ycor (float): y-ova souradnice leveho dolniho rohu (jihozapadni roh)
    zcor (float): z-ova souradnice leveho dolniho rohu (jihozapadni roh)
    height (int): vyska veze
    size (int): sirka/delka veze
  '''

  # postavi sloupec ze ctvercu naskladanych na sobe
  for row in range(height):
    ctverec(xcor, ycor+row, zcor, size)

  # prida vezi sloupci hradby, aby vysledek vypadal jako vez
  ctverec(xcor-1, ycor+height, zcor-1, size+2)
  ctverec(xcor-1, ycor+height+1, zcor-1, size+2, True)

  # udela podlahu veze
  for zrow in range(size-2):
    for xrow in range(size-2):
      st.Hranol(xcor+1+xrow, ycor+height-1, zcor+1+zrow, barva= (0.8, 0.8, 0.8))


def cimburi(xcor: float, ycor: float, zcor: float) -> None:
  '''
  Postavi cimburi

  Args:
    xcor (float): vychazi z definice procedury kruh() (cimburi ma kruhovy pudorys)
    ycor (float): vychazi z definice procedury kruh() (cimburi ma kruhovy pudorys)
    zcor (float): vychazi z definice procedury kruh() (cimburi ma kruhovy pudorys)
  '''

  # postavi valec dane vysky (zaklad cimburi)
  for row in range(HGHT_CIMB):
    kruh(xcor, ycor+row+HGHT*4, zcor, RESOLUTION, DIAM)

  # postavi valci hradby, aby vypadal jak cimburi
  for row in range(3):
    kruh(xcor, ycor+HGHT_CIMB+row+HGHT*4, zcor, RESOLUTION, DIAM+0.25, 2-row == 0)


def hrad(xcor: float, ycor: float, zcor: float) -> None:
  '''
  Postavi hrad se ctyrmi vezemi a cimburim

  Args:
    xcor (float): x-ova souradnice leveho dolniho rohu (jihozapadni roh)
    ycor (float): y-ova souradnice leveho dolniho rohu (jihozapadni roh)
    zcor (float): z-ova souradnice leveho dolniho rohu (jihozapadni roh)
  '''

  vez(xcor, ycor, zcor, HGHT, SIZE) # postavi zaklad hradu bez vezi a cimburi

  #postavi ctyri veze (dva cykly urcuji ktera vez se stavi na zaklade svetovych stran)
  for north in range(2):
    for east in range(2):
      vez(xcor+east*SIZE*(3/4), ycor+HGHT, zcor+north*SIZE*(3/4), int(HGHT*(3/4)), int(SIZE/4))

  cimburi(xcor+SIZE/2-1, ycor-1, zcor+SIZE/2) # postavi cimburi

hrad(XCOR, YCOR, ZCOR) # postavi hrad
st.ZobrazScenu()
