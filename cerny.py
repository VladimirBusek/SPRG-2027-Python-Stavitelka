import stavitelka as st 
import random

velikost = 40
velikost = (velikost + 10) // 20 * 20
if velikost < 20:
    velikost = 20

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


while (y<=velikost/10):
    while (z<=velikost):
        cihla(x,y,z,0,0,0)
        x+= 4
        r = random.randint(0,1)
        g = random.randint(0,1)
        b = random.randint(0,1)
        if (x == velikost):
            x = 0
            z+=2
    z = 0
    y+=1



y = velikost/10

while (y<=velikost/2):
    while (z<velikost/5):
        cihla(x,y,z,0,0,0)
        x+= 4
        r = random.randint(0,1)
        g = random.randint(0,1)
        b = random.randint(0,1)
        if (x >= velikost/5):
            x = 0
            z+=2
    z = 0
    y+=1

y = velikost/10

while (y<=velikost/2):
    x = velikost - 4
    z = 0
    while (z<velikost/5):
        while (x>=velikost-velikost/5):
            r = random.randint(0,1)
            g = random.randint(0,1)
            b = random.randint(0,1)
            cihla(x,y,z,0,0,0)
            x -= 4
        x = velikost-4
        z += 2 
    y+=1

y = velikost/10

while (y<=velikost/2):
    x = velikost - 4
    z = velikost
    while (z>=velikost-velikost/5):
        while (x>=velikost-velikost/5):
            r = random.randint(0,1)
            g = random.randint(0,1)
            b = random.randint(0,1)
            cihla(x,y,z,0,0,0)
            x -= 4
        x = velikost-4
        z -= 2 
    y+=1

y = velikost/10

while (y<=velikost/2):
    x = 0
    z = velikost
    while (z>=velikost-velikost/5):
        while (x<velikost/5):
            r = random.randint(0,1)
            g = random.randint(0,1)
            b = random.randint(0,1)
            cihla(x,y,z,0,0,0)
            x += 4
        x = 0
        z -= 2 
    y+=1





x = 0
y = 0
z = velikost
posun = 4
cimburi = False


while (y<=velikost/4) and not cimburi:
    x = 0
    z = velikost
    while (z>=velikost-2):
        while (x<velikost):
            r = random.randint(0,1)
            g = random.randint(0,1)
            b = random.randint(0,1)
            cihla(x,y,z,0,0,0)
            x += posun
            if (posun == 8):
                cimburi = True
                
        x = 0
        if not cimburi:
            z -= 2 
        else: break
    y+=1
    if (y>=velikost/4):
        posun = 8


st.Hranol(x,0,z,1,50,1,0,0,0,(1,0,0))
print(x)
print(y)
print(z)
print("Velikost:",velikost)
input()
st.ZobrazScenu()
