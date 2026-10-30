import stavitelka as st 
import random

r = 1
b = 1
g= 1

def cihla(x,y,z,rx,ry,rz):
    st.Hranol(x=x,y=y,z=z,sx=4,sy=1,sz=2,rx=rx,ry=ry,rz=rz,barva=(r,g,b,))

x = 0
rx=0
y = 0
ry=0
z = 0
rz=0

while (z<26):
    cihla(x,0,z,0,0,0)
    x+= 4
    r = random.randint(0,1)
    g = random.randint(0,1)
    b = random.randint(0,1)
    if (x == 40):
        x = 0
        z+=2
z = 0

#while (y<2)
 #   cihla(x,y,z,rx,ry,rz)





st.ZobrazScenu()
