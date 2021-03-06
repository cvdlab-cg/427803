from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/toucherjay/Desktop/lar-cc/lib/py')
from larcc import *
from sysml import *
from splines import *
from architectural import *
from exercise1 import *
from mapper import *
from simplexn import *
from lar2psm import *

GRID = COMP([INSR(PROD),AA(QUOTE)])

DRAW = COMP([VIEW,STRUCT,MKPOLS])

"""Appartamento"""

master = assemblyDiagramInit([7,15,2])([[.3,2,.3,4,.3,1.5,.05],[.3,1,0.3,0.2,.05,3,.1,2,.1,.4,.05,1.3,.1,3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))

#in cyan i numeri delle celle
casa = cellNumbering (master,hpc)(range(len(CV)),CYAN,1)
#VIEW(casa)

#RIMOZIONE CELLE
remove = [0,1,2,3,30,31,32,33,150,151,152,153,180,181,182,183,154,155,184,185,156,157,186,187,178,179,176,177,174,175,172,173,203,202,204,205,206,207,208,209]

#cubicroom
roomsToRemove = [37,41,45,49,53,57,93,97,101,105,109,113,117,161,163,165,167,169]

#pareti
wallsToRemove = [39,43,47,51,55,69,67,71,95,99,111]
#pavimenti
#floorsToRemove = [130,152,174,196,218,128,216,150,172,194,238,240]

toRemove = roomsToRemove + wallsToRemove + remove 


#in CV di master inserisco solo le celle NON da rimuovere
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)


#CREAZIONE PORTE E FINESTRE NELLE PARETI
#porta d'entrata (cella 27)
diagram = assemblyDiagramInit([2,1,2])([[1.7,.3],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,27)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)

#porta camera (cella 53)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.5,1,.5],[2.2,.5]])
#diagram = assemblyDiagramInit([1,1,2])([[.3],[1],[2.2,.5]])
master = diagram2cell(diagram,master,52)


#VIEW(hpc)
#porta bagno (cella 61)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.15,.7,.15],[2.2,.5]])
master = diagram2cell(diagram,master,59)

#VIEW(hpc)
#porta camera-letto (cella 65)
diagram = assemblyDiagramInit([1,3,2])([[.3],[1,1,1],[2.2,.5]])
master = diagram2cell(diagram,master,62)

#VIEW(hpc)

#finestra soggiorno/balcone (cella 99)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.8,1.4,.8],[2.2,.5]])
master = diagram2cell(diagram,master,95)

#VIEW(hpc)

#finestra camera/balcone (cella 103)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.65,.7,.65],[2.2,.5]])
master = diagram2cell(diagram,master,98)

#VIEW(hpc)
#finestra1 bagno (cella 111)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.625,.7,.625],[1,1.4,.3]])
master = diagram2cell(diagram,master,105)


#VIEW(hpc)
#finestra2 camera (cella 115)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.8,1.4,.8],[1,1.4,.3]])
master = diagram2cell(diagram,master,108)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)

#RIMOZIONE PORTE E FINESTRE
porte = [133,139,145,151]
finestre = [180,171]
balconi = [163, 157]
balcone = [110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132]
toRemove2 = porte + finestre + balconi + balcone
master0 = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove2)]
#DRAW(master0)

"""Assemblaggio Palazzina"""
floor0 = STRUCT(MKPOLS(master0))
floor1 = T(3)(3)(STRUCT(MKPOLS(masterF)))
floor2 = T(3)(3)(floor1)
floor3 = T(3)(3)(floor2)
floor4 = T(3)(3)(floor3)

tetto = COLOR([0.95,0.90,0.87])(T([1,2,3])([-6.9,-12.2,15])(CUBOID([13.8,24.4,0.5])))
alaE = STRUCT([floor0,floor1,floor2,floor3,floor4])
VIEW(alaE)
alaO = T(1)(0)(R([2,2])(3/2*(PI))(alaE))
alaFRONT = STRUCT([alaO,alaE])
alaBACK = R([1,2])(PI)(alaFRONT)
portone = T(2)(-1)(CUBOID([8.45,2,2.7]))

"""Pianerottolo"""
pianerottolo = COLOR([0.95,0.90,0.87])(T([1,2])([-5,-1.5])(CUBOID([15,3,.3])))
piano_back = (T([1,2])([-6.8,-1.5])(CUBOID([2,3,.3])))

"""Ingresso Palazzo"""
muro_androne = CUBOID([4.3,0.3,3])
m_andr_sx = T([1,2])([2.6,-1.5])(muro_androne)
m_andr_dx = T([1,2])([2.6,1.2])(muro_androne)

"""Lato Scale Ala Back"""
ala_scale = T([1,2])([-6.9,-1.3])(CUBOID([4.6,2.6,15]))
alaFRONT_complete = DIFFERENCE([alaFRONT,portone])
alaBACK_complete = DIFFERENCE([alaBACK,ala_scale])

#SCALE
DRAW = COMP([VIEW,STRUCT,MKPOLS])
master_scale = assemblyDiagramInit([4,3,2])([[.3,1.6,2.6,5.2],[.3,2.6,.3],[.3,2.7]])
V,CV = master_scale
hpc = SKEL_1(STRUCT(MKPOLS(master_scale)))
hpc = cellNumbering (master_scale,hpc)(range(len(master_scale[1])),RED,1)
#VIEW(hpc)

toRemoveScale = [23,21,19,15,9,8]
master_scale = master_scale[0], [cell for k,cell in enumerate(master_scale[1]) if not (k in toRemoveScale)]

#Finestre scale
diagram = assemblyDiagramInit([1,3,3])([[.3],[.6,1.4,.6],[1,1.4,.3]])
master_scale = diagram2cell(diagram,master_scale,3)

hpc = SKEL_1(STRUCT(MKPOLS(master_scale)))
hpc = cellNumbering (master_scale,hpc)(range(len(master_scale[1])),RED,1)
#VIEW(hpc)

#Rimuove finestre
removeFinestre = [21]
master_scale = master_scale[0], [cell for k,cell in enumerate(master_scale[1]) if not (k in removeFinestre)]

DRAW(master_scale)

piano_scale = T([1,2])([-6.9,-1.6])(STRUCT(MKPOLS(master_scale)))
pscale0 = T(3)(3)(piano_scale)
pscale1 = T(3)(3)(pscale0)
pscale2 = T(3)(3)(pscale1)
pscale3 = T(3)(3)(pscale2)

scale = STRUCT([piano_scale,pscale0,pscale1,pscale2,pscale3])


#FINESTRE
glass_mat = [0,0.19,0.39,1, 0,0,0,0.2, 0,0,0,1, 0,0,0,1, 100]

#Finestre Scale
wglass1 = CUBOID([.1,1.4,1.4])
wglass1 = T([1,2,3])([-6.9,-.7,1.3 ])(wglass1)
wglass1 = MATERIAL(glass_mat)(wglass1)
wglass2 = T(3)(3)(wglass1)
wglass3 = T(3)(3)(wglass2)
wglass4 = T(3)(3)(wglass3)
wglass5 = T(3)(3)(wglass4)

#material:  	     ambient         diffuse  specular emission shininess
finestre_scala = STRUCT([wglass1,wglass2,wglass3,wglass4,wglass5])

#Finestre Palazzo

#Balcone Living
glassLiving = CUBOID([.1,1.4,2.2])
glassLiving = T([1,2,3])([6.8,2.65,.3])(glassLiving)
glassLiving = MATERIAL(glass_mat)(glassLiving)
glassLivingMirrored = T(2)(-6.7)(glassLiving)
glassLivingBase = STRUCT ([glassLiving, glassLivingMirrored])
glassLiving1 = T(3)(3)(glassLivingBase)
glassLiving2 =	T(3)(3)(glassLiving1)
glassLiving3 = T(3)(3)(glassLiving2)
glassLiving4 = T(3)(3)(glassLiving3)

finestre_living = STRUCT([glassLivingBase,glassLiving1,glassLiving2,glassLiving3,glassLiving4])
finestre_living_post = T(1)(-13.6)(finestre_living)

#Balcone Camera
glassRoom = CUBOID([.1,.7,2.2])
glassRoom = T([1,2,3])([6.8,5.6,.3])(glassRoom)
glassRoom = MATERIAL(glass_mat)(glassRoom)
glassRoomMirrored = T(2)(-11.9)(glassRoom)
glassRoomBase = STRUCT([glassRoom, glassRoomMirrored])
glassRoom1 = T(3)(3)(glassRoomBase)
glassRoom2 = T(3)(3)(glassRoom1)
glassRoom3 = T(3)(3)(glassRoom2)
glassRoom4 = T(3)(3)(glassRoom3)

finestreRoom = STRUCT ([glassRoomBase, glassRoom1, glassRoom2, glassRoom3,glassRoom4])
finestreRoomBack = T(1)(-13.6)(finestreRoom)

#Finestra Bagno
glassBath = CUBOID([.1,.47,1.4])
glassBath = T([1,2,3])([6.8,7.915,1.3])(glassBath)
glassBath = MATERIAL(glass_mat)(glassBath)
glassBathMirrores = T(2)(-16.3)(glassBath)
glassBathBase = STRUCT ([glassBath, glassBathMirrores])
glassBath1 = T(3)(3)(glassBathBase)
glassBath2 = T(3)(3)(glassBath1)
glassBath3 = T(3)(3)(glassBath2)
glassBath4 = T(3)(3)(glassBath3)

finestreBath = STRUCT ([glassBathBase, glassBath1, glassBath2, glassBath3, glassBath4])
finestreBathBack = T(1)(-13.6)(finestreBath)

#FinestraBed
glassBed = CUBOID([.1,1.4,1.4])
glassBed = T([1,2,3])([6.8,9.7,1.3])(glassBed)
glassBed = MATERIAL(glass_mat)(glassBed)
glassBedMirrored = T(2)(-20.8)(glassBed)
glassBedBase = STRUCT ([glassBed, glassBedMirrored])
glassBed1 = T(3)(3)(glassBedBase)
glassBed2 = T(3)(3)(glassBed1)
glassBed3 = T(3)(3)(glassBed2)
glassBed4 = T(3)(3)(glassBed3)

finestreBed = STRUCT([glassBedBase, glassBed1, glassBed2, glassBed3, glassBed4])
finestreBedBack = T(1)(-13.6)(finestreBed)



#Scala
stair = spiralStair(width=0.1,R=1,r=0.25,riser=0.1,pitch=4.4,nturns=1.5,steps=30)
stair = larApply(r(0,0,2*PI))(stair)
stair = larApply(t(-5,0,0))(stair)
stairColumn = larApply(t(-5,0,0))(larRod(0.1,3.3)())
stairs3D = evalStruct(Struct([stairColumn,stair,t(0,0,3)]*4))
stairs = COLOR([0.95,0.90,0.87])(STRUCT(CAT(AA(MKPOLS)(stairs3D))))
#VIEW(stairs)

#Balcone
baseBalcone = CUBOID([1.6,5.7,.3])
palettoRinghiera = CUBOID([0.05,0.05,0.65])
paletti = STRUCT(NN(38)([palettoRinghiera,T(2)(0.15)]))
paletti = T(3)(0.3)(paletti)
palettoRinghieraX = palettoRinghiera
palettoRinghieraX = T([1,2])([1,2])(palettoRinghieraX)
palettiX = STRUCT(NN(10)([palettoRinghiera,T(2)(0.15)]))
palettiX = R([1,2])(PI/2)(palettiX)
palettiX = T([1,3])([1.5,0.3])(palettiX)
upRinghieraY = CUBOID([0.05,5.7,0.05])
upRinghieraY = T(3)(0.95)(upRinghieraY)

upRinghieraX = CUBOID([1.6,0.05,0.05])
upRinghieraX = T(3)(0.95)(upRinghieraX)
upRinghieraX  =STRUCT(NN(2)([upRinghieraX,T(2)(5.65)]))
palettiX = STRUCT(NN(2)([palettiX,T(2)(5.65)]))
upRinghiera = STRUCT([upRinghieraX,upRinghieraY])
balcone = STRUCT([baseBalcone,paletti,upRinghiera,palettiX])
balconeSxAnt = T([1,2,3])([8.45,-1.8,3])(R([1,2])(PI)(balcone))
balconeSxAnt1 = T(3)(3)(balconeSxAnt)
balconeSxAnt2 = T(3)(3)(balconeSxAnt1)
balconeSxAnt3 = T(3)(3)(balconeSxAnt2)
balconiSxA = STRUCT([balconeSxAnt,balconeSxAnt1,balconeSxAnt2,balconeSxAnt3])
balconiDxA = T(2)(9.3)(balconiSxA)
balconiAnt = COLOR([0.95,0.90,0.87])(STRUCT([balconiSxA,balconiDxA]))
balconiPost = COLOR([0.95,0.90,0.87])(R([1,2])(PI)(balconiAnt))


#Portone
portone = T([1,2])([6.6,-1])(CUBOID([.3,2,2.7]))
portone = MATERIAL(glass_mat)(portone)
cornice = COLOR([0.95,0.90,0.87])(T([1,2])([6.9,-1])(CUBOID([0.01,.2,2.7])))
corniceD = T(2)(1.8)(cornice)
corniceM = T(2)(.9)(cornice)
corniceS = COLOR([0.95,0.90,0.87])(T([1,2,3])([6.9,-1,2.7])(CUBOID([0.01,2,.3])))
portoneC = STRUCT([portone, cornice,corniceD,corniceS,corniceM])

#PORTE CASE
muro_androne = CUBOID([2,0.3,2.5])
porta_sx = COLOR([0.6,0.4,0])(T([1,2])([.3,-1.6])(muro_androne))
porta_dx = COLOR([0.6,0.4,0])(T([1,2])([.3,1.3])(muro_androne))
porte_avanti = STRUCT([porta_sx,porta_dx])
porte_dietro = T(1)(-2.3)(porte_avanti)
porte_terra = STRUCT([porte_avanti,porte_dietro])
porte1 = T(3)(3)(porte_terra)
porte2 = T(3)(3)(porte1)
porte3 = T(3)(3)(porte2)
porte4 = T(3)(3)(porte3)

porte_tot = STRUCT ([porte_terra, porte1, porte2, porte3,porte4])

#Prato
controlpoints = [[20,0],[22,0],[24,0],[26,-1],[28,-4],[29,-7],[30,-10]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva = STRUCT(MKPOLS(obj))
hill = (STRUCT([curva,S(1)(-1)(curva),POLYLINE([[-20,0],[20,0]]),POLYLINE([[-30,-10],[30,-10]])]))
hill2D = COLOR([0.002,0.743,0.224])(PROD([SOLIDIFY(hill),Q(.1)]))
hill2Ddx = R([1,2])(PI)(hill2D)
hill2D3 = R([1,2])(PI/2)(STRUCT ([hill2D,hill2Ddx]))
hill2D4 = R([1,2])(SQRT(2)*PI/2)(STRUCT ([hill2D,hill2Ddx]))
hill2D5 = R([1,2])(SQRT(2)*-PI/2)(STRUCT ([hill2D,hill2Ddx]))
prato = STRUCT([hill2D,hill2Ddx,hill2D3, hill2D4, hill2D5])


#hill3D = T(3)(-0.1)(STRUCT(NN(36)([hill2D,R([1,2])(PI/36)])))
hillT = R([1,2])(PI/4)(hill2D)
VIEW(hill2D)

#recinto
parall = T([1,2])([12.8,1.5])(CUBOID([.2,5.7,1]))
perpen1 = T([1,2])([6.9,1.5])(CUBOID([6,.2,1]))
perpen2 = T([1,2])([6.9,7])(CUBOID([6,.2,1]))

recintodx = COLOR([0.95,0.90,0.87])(STRUCT([parall,perpen1,perpen2]))
recintosx = COLOR([0.95,0.90,0.87])(T(2)(-8.7)(recintodx))
recintoAnt = STRUCT([recintodx,recintosx])
recintoPost = R([1,2])(PI)(recintoAnt)

alaBACK_scale = STRUCT([alaBACK_complete,scale])
palazzo_noBalconi = STRUCT([alaFRONT_complete,alaBACK_scale,pianerottolo,piano_back,tetto])
VIEW(STRUCT([palazzo_noBalconi,stairs,finestre_scala,finestre_living, finestre_living_post, finestreRoom,finestreRoomBack,finestreBath, 
	finestreBathBack, finestreBed, finestreBedBack, balconiAnt, balconiPost, portoneC, m_andr_sx,m_andr_dx, porte_tot, recintoAnt, recintoPost, prato]))





