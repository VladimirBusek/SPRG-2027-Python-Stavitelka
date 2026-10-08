######################################################################
# stavitelka
#    Modul pro vytváření a zobrazení 3D scény
# ---------------------------------------------------------
# Příklad:
# --------------------------
# import stavebnice3d as st
# st.Hranol()
# st.ZobrazScenu()
# --------------------------
#
# Podrobnější informace: https://web.geometry.cz/stavitelka
#
# (C) Šárka a Tom, 2023-24, under CC BY-NC
# mail: tom@geometry.cz
#
# verze: 12.08.2024 17:33:24
######################################################################

default_color = (1,1,1)
DEFAULT_COLOR = "DC"

def Hranol( x=0,y=0,z=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, barva=DEFAULT_COLOR ):
    """Sestrojí hranol

    Parametry:
    ----------
    x, y, z    : poloha
    sx, sy, sz : zvětšení v jednotlivých směrech
    rx, ry, rz : rotace podle jednotlivých os,
                 rotuje se v pořadí 1) podle osy Z, 2) podle osy X a 3) podle osy Y
                 transformuje se v pořadí I) zvětšení, II) rotace, III) poloha
    barva      : barva; pokud je rovna DEFAULT_COLOR, použije se proměnná default_color
    """
    Tvar( "C", x,y,z, sx, sy, sz, rx, ry, rz, barva )

def Koule( x=0,y=0,z=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, barva=DEFAULT_COLOR ):
    """Sestrojí kouli

    Parametry:
    ----------
    x, y, z    : poloha
    sx, sy, sz : zvětšení v jednotlivých směrech
    rx, ry, rz : rotace podle jednotlivých os,
                 rotuje se v pořadí 1) podle osy Z, 2) podle osy X a 3) podle osy Y
                 transformuje se v pořadí I) zvětšení, II) rotace, III) poloha
    barva      : barva; pokud je rovna DEFAULT_COLOR, použije se proměnná default_color
    """
    Tvar( "S", x,y,z, sx, sy, sz, rx, ry, rz, barva )

def Valec( x=0,y=0,z=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, barva=DEFAULT_COLOR ):
    """Sestrojí válec

    Parametry:
    ----------
    x, y, z    : poloha
    sx, sy, sz : zvětšení v jednotlivých směrech
    rx, ry, rz : rotace podle jednotlivých os,
                 rotuje se v pořadí 1) podle osy Z, 2) podle osy X a 3) podle osy Y
                 transformuje se v pořadí I) zvětšení, II) rotace, III) poloha
    barva      : barva; pokud je rovna DEFAULT_COLOR, použije se proměnná default_color
    """
    Tvar( "Y", x,y,z, sx, sy, sz, rx, ry, rz, barva )

def TVAR_zacatek_definice( jmeno ):
    """Dále vytvářené tvary budou znamenat definici nového tvaru

    Parametry:
    ----------
    jmeno : jméno
    """
    prikaz = f"DEF {jmeno}"
    in_def = 1
    Zapis( prikaz )

def TVAR_konec_definice():
    """Ukončuje definici"""
    prikaz = f"ENDDEF"
    in_def = 0
    Zapis( prikaz )

def TVAR( tvar, x=0,y=0,z=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, barva=DEFAULT_COLOR ):
    """Sestrojí tvar "tvar" podle dříve uložené definice

    Parametry:
    ----------
    x, y, z    : poloha
    sx, sy, sz : zvětšení v jednotlivých směrech
    rx, ry, rz : rotace podle jednotlivých os,
                 rotuje se v pořadí 1) podle osy Z, 2) podle osy X a 3) podle osy Y
                 transformuje se v pořadí I) zvětšení, II) rotace, III) poloha
    barva      : barva; pokud je rovna DEFAULT_COLOR, použije se proměnná default_color
    """
    Tvar( tvar, x,y,z, sx, sy, sz, rx, ry, rz, barva )    

def Pohled( x=0,y=0,z=0, rx=0, ry=0, rz=0 ):
    """Nastavuje pozici a rotaci kamery

    Parametry:
    ----------
    x, y, z    : poloha
    rx, ry, rz : rotace podle jednotlivých os,
                 rotuje se v pořadí 1) podle osy Z, 2) podle osy X a 3) podle osy Y
    """
    Zapis( f"M P {x} {y} {z}  R {rx} {ry} {rz}" )

# ---------------------------------------------------------    

in_def = 0

vystup = []

def Zapis( prikaz ):
    vystup.append( prikaz )
    #print( prikaz )

def Par( PAR, x,y,z, default ):
    vys = ""

    if (x,y,z)!=(default, default, default):
        vys = f"{PAR} {x} {y} {z}"
        return vys
    
    if x!=default:
        vys += f"{PAR}x {x}"
    if y!=default:
        vys += f"{PAR}y {y}"
    if z!=default:
        vys += f"{PAR}z {z}"
    return vys

def Par3( PAR, xyz, default ):
    vys = ""
    if xyz!=default:
        vys += f"{PAR} {xyz[0]} {xyz[1]} {xyz[2]}"
    return vys


def Tvar( tvar, x,y,z, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, color=DEFAULT_COLOR ):
    if color == DEFAULT_COLOR:
        color = default_color
    indent = ' '*(3*in_def)    
    params = f'{Par("P", x,y,z, 0)} {Par("S", sx,sy,sz, 1)} {Par("R", rx, ry, rz, 0)}' \
             +f' {Par3("C", color, (1,1,1))}'
    prikaz = f"{indent}{tvar} {params}"
    Zapis( prikaz )
    




def ZkopirujVystupDoSchranky():
    from tkinter import Tk # in Python 2, use "Tkinter" instead 
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    #r.clipboard_append('i can has clipboardz?')
    r.clipboard_append("\n".join( vystup ))
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()


import webbrowser

def ZobrazScenu():
    filedata = zacatek + ('\n'.join(vystup)) + konec
    url="nove.html"

    with open(url, 'w') as file:
        file.write(filedata)
    file.close()  
  
    webbrowser.open_new_tab(url)

################# data: ... ##########################################
zacatek= '''
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
    <style>
* {
  box-sizing: border-box;
}
body, button, input {
  background-color: #ffffee;
  font-size:20px;
}

.header, .footer {
  background-color: maroon;
  color: white;
  padding: 2px;
}

.column {
  float: left;
  padding: 5px;
}

.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

.popis {
  width: 28%;
  padding: 5px;
}

.content {
 position: static;
  width: 70%;
}

</style>
    <script type='text/javascript' src='https://www.x3dom.org/download/x3dom.js'> </script>
    <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/download/x3dom.css'/>	</head>
	<body>
    <div class="header">      &nbsp;    </div>
    <div class="clearfix">
    <div class="column popis"> 
     <form >
     <p><label for="fname">Scéna:</label></p>
       <textarea name="vstup" id="vstup" rows="40" cols="60">
'''
konec='''
</textarea>    
      <p><input type="button" value="Zobraz" onclick="uklid();init();dopln(data);"></p>   <!--location.reload(); x3dom.reload(); -->
     </form>
    </div>

    <div class="column content">
	<p>3D view:</p>
	<a href="https://projektor.geometry.cz">Projektor</a>
	<X3D id='skladacka' height="70vh" >     <!-- width="900" height="500"-->
  <Scene DEF='scene'>

<!--------------------Tohle je misto na nove tvary ------------------->
    
    <Group visible='false' id="uzivatelske">     
    </Group>
    
<!----------------------KONEC -------------------->
   
        <WorldInfo title='Prototyp sceny'></WorldInfo>
        <Viewpoint id="front" description='Zpredu' orientation='1 0 0 -0.13' position='0 2.3 15' fieldOfView='0.55' bind='true'></Viewpoint>
        <Viewpoint id="top" description='Shora' orientation='1 0 0 -1.7' position='0 12 -1' fieldOfView='0.5'></Viewpoint>
        <Viewpoint id="left" position="-12 0 -1" orientation="0 1 0 -1.7" description='Zleva'></Viewpoint>
        <Viewpoint id="right" position="12 0 -1" orientation="0 1 0 1.7" description='Zprava'></Viewpoint>
        <Background groundAngle='0.05 1.52 1.56 1.5707' groundColor='0.5 0.8 0 0.5 0.8 0 0.5 0.8 0.3 0.2 0.8 0.2 0 0.8 0.2' skyAngle='0.04 0.05 0.1 1.309 1.570' skyColor='0.8 0.8 0.2 0.8 0.8 0.2 0.1 0.1 0.6 0.1 0.1 0.6 0.1 0.25 0.8 0.6 0.6 0.9'/></Background>
        <NavigationInfo id="navidef" type='"any"' bind='true'></NavigationInfo>
        <NavigationInfo id="navilook" type='"lookat"'></NavigationInfo>
	    <NavigationInfo id="naviwalk" type='"walk"'></NavigationInfo>
	    <NavigationInfo id="navifly" type='"fly"'></NavigationInfo>
        <NavigationInfo id="naviexp" type='"explore"'></NavigationInfo>
	    <NavigationInfo id="navinone" type='"none"'></NavigationInfo>
        
<!--------------------Tohle scena prelozena z vygenerového py ------------------->
        <Group>
        <Group id="semPridat">
        </Group>
        <DirectionalLight ambientIntensity='0' color='1,1,0.5' direction='-0.4,-0.8,-1' global='true' intensity='0.5' on='true' shadowCascades='1' shadowFilterSize='20' shadowIntensity='0.7' shadowMapSize='4096' shadowOffset='0.8' shadowSplitFactor='0.9' shadowSplitOffset='0.05' zFar='-1' zNear='-1' ></DirectionalLight> 
        </Group>
<!----------------------KONEC -------------------->

      </Scene>
  	</X3D>
    <p style="display:inline-block; width:40%;">
    <button onclick="document.getElementById('front').setAttribute('set_bind','true');">Front</button>
    <button onclick="document.getElementById('top').setAttribute('set_bind','true');">Top</button>
    <button onclick="document.getElementById('left').setAttribute('set_bind','true');">Left </button>
    <button onclick="document.getElementById('right').setAttribute('set_bind','true');">Right </button>
    <button onclick="vychozi()">Def</button>
    </p>
    <p style="display:inline-block; text-align: right; width:59%;">
    <button onclick="document.getElementById('navidef').setAttribute('set_bind','true');gonavidef();">DEFAULT</button>
    <button onclick="document.getElementById('navilook').setAttribute('set_bind','true');">LOOK-AT</button>
    <button onclick="document.getElementById('naviwalk').setAttribute('set_bind','true');">WALK</button>
    <button onclick="document.getElementById('navifly').setAttribute('set_bind','true');">FLY </button>
    <button onclick="document.getElementById('naviexp').setAttribute('set_bind','true');">EXPLORE </button>
    <button onclick="document.getElementById('navinone').setAttribute('set_bind','true');">NONE</button>
    </p>
    </div>
    </div>
    <div class="footer">&nbsp;</div>
    
    <script type="text/javascript">
      var maxz = 0;
      var vdefinici = false;
      var ntvar = document.createElement('Null');
      var noveId = '';
      var data = '';
      var pk = '0 2.3 15';
      
      function vychozi(){
      document.getElementById('front').setAttribute('set_bind','true');document.getElementById('front').setAttribute('position',pk);
      }
      
      function gonavidef(){ 
      //document.getElementById('front').setAttribute('position','0, 2.3 '+(maxz+15).toString());
      document.getElementById('front').setAttribute('orientation','1 0 0 -0.13');
      document.getElementById('front').setAttribute('fieldOfView','0.55');
      document.getElementById('front').setAttribute('set_bind','true');
      }      

      function init() {
      data=document.getElementById('vstup').value;
      }
      
      function loadItems(radek){
         PI = 3.14159265358;
         parms=radek.split(" ");
         
         if (parms[0]=="DEF"){
         vdefinici = true;    
         var ntvar = document.createElement('Group');
         ntvar.setAttribute('DEF', parms[1]);
         ntvar.setAttribute('id', parms[1]);
         noveId = parms[1];
         uzivatelske.appendChild(ntvar);
         } 
         else if (parms[0]=="ENDDEF"){ vdefinici = false;
         }
         else if (parms[0]=="M"){ iP = parms.indexOf('P',1); if (iP<0){pk = '0 2.3 15'}  else {pk = ' ' + parms[iP+1] + ' ' +  parms[iP+2] + ' ' + -parms[iP+3];}
         } 
         else {          
         iP = parms.indexOf('P',1); if (iP<0){p = '0 0 0'}  else {p = ' ' + parms[iP+1] + ' ' +  parms[iP+2] + ' ' + -parms[iP+3];}
         iS = parms.indexOf('S',1); if (iS<0){s = '1 1 1'}  else {s = ' ' + parms[iS+1] + ' ' +  parms[iS+2] + ' ' + parms[iS+3];}
         iC = parms.indexOf('C',1); if (iC<0){c = '1 1 1'}  else {c = ' ' + parms[iC+1] + ' ' +  parms[iC+2] + ' ' + parms[iC+3];}
         iR = parms.indexOf('R',1); if (iR<0){ rx = '1 0 0 0'; ry = '0 1 0 0'; rz = '0 0 1 0'}  
         else { 
         rx = '1 0 0 '+ parms[iR+1]/180*(-PI);
         ry = '0 1 0 '+ parms[iR+2]/180*(-PI);
         rz = '0 0 1 '+ parms[iR+3]/180*PI;  
         }         
         var uzel = document.createElement('Transform');
         uzel.setAttribute('translation', ' ' + p);
         uzel.setAttribute('rotation', ry);
         var tra2 = document.createElement('Transform');
         tra2.setAttribute('rotation', rx);
         uzel.appendChild(tra2);
         var tra3 = document.createElement('Transform');
         tra3.setAttribute('rotation', rz);
         tra3.setAttribute('scale', ' ' + s);
         tra2.appendChild(tra3);
         var prvek = document.createElement('Shape');
         if (parms[0].length>1){
         prvek.setAttribute('USE', parms[0]);
         prvek.setAttribute('visible', 'true');
         } else { 
            var vzhled = document.createElement('Appearance');
            var material = document.createElement('Material'); material.setAttribute('diffuseColor', ' '+ c);
            
            if (parms[0]=='S'){var geometrie = document.createElement('Sphere'); geometrie.setAttribute('radius', '0.5');}
            else if (parms[0]=='C'){var geometrie = document.createElement('Box'); geometrie.setAttribute('size', '1,1,1');}     
            else if (parms[0]=='Y'){var geometrie = document.createElement('Cylinder'); geometrie.setAttribute('radius', '0.5'); geometrie.setAttribute('height','2.0');}
            vzhled.appendChild(material);
            prvek.appendChild(vzhled);
            prvek.appendChild(geometrie);
         }
         tra3.appendChild(prvek); 
         if (vdefinici){document.getElementById(noveId).appendChild(uzel); 
         }  else {semPridat.appendChild(uzel);}        
         }
         }
         
         function uklid(){
         var grtyp = document.getElementById("uzivatelske");
         while (grtyp.firstChild) {
           pryc = grtyp.removeChild(grtyp.firstChild);
         }
         var grsc = document.getElementById("semPridat");
         while (grsc.firstChild) {
           pryc = grsc.removeChild(grsc.firstChild);
         }
         }

        function dopln(data) {
        var lines = data.split('\\n'); 
        for (i=0; i<lines.length; i++) {
            linka=lines[i].trim(); 
            if (linka.length>0){loadItems(linka);}
            }
        }
        
      init();
      dopln(data);
      document.getElementById('front').setAttribute('position',pk);
    </script>     
	</body>
</html>         
'''
    

