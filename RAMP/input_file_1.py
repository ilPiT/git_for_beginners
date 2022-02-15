# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:59:59 2021

@author: Clau
"""

'''
Paper: Energy sufficiency, lowlands.
SCENARIO 4 
'''

from core import User, np
User_list = []

##Prova di utilizzo di git
##Prova a caricare su diverse branch
# Prova pull su una diversa branch dal main

### We are keeping the percentage of HH LI at 96%
####it would be interesting also to have the profile of the HH LI and HH HI to see how it is distribuited the energy consumption

#Defining users (14 users but with the school type B) and helath center instead of the helath post

H1 = User("low income", 480)
User_list.append(H1)

H2 = User("high income", 20)
User_list.append(H2)

HC = User("Health center", 1)
User_list.append(HC)

SB = User("School type B", 1)
User_list.append(SB)

Public_lighting = User("Public lighting ", 12)
User_list.append(Public_lighting)

WSS = User("water supply system", 2)
User_list.append(WSS)

GS = User("Grocery Store 1", 4)
User_list.append(GS)

IW = User("Irrigation Water", 15)
User_list.append(IW)

#Appliances
#Low Income Households
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35,[0,30])

H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)


'''#High income households
H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([1082,1440],[0,60],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5)
H2_DVD.windows([1082,1440],[0,60],0.35)

H2_Antenna = H2.Appliance(H2,1,8,2,80,0.1,5)
H2_Antenna.windows([1082,1440],[0,60],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,30],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30, 'yes',2)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(5,15,200,15)
H2_Freezer.specific_cycle_2(200,10,5,20)
H2_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Fan = H2.Appliance(H2,1,171,1,220,0.27,60)
H2_Fan.windows([720,1080],[0,0],0.35)

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0],0.35)
'''
#Health Center
HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(HC,2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_fan = HC.Appliance(HC,2,60,1,240,0.2,60)
HC_fan.windows([660,960],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30)
HC_sterilizer_stove.windows([540,600],[900,960],0.35)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.2,10)
HC_needle_destroyer.windows([540,600],[0,0],0.35)

HC_water_pump = HC.Appliance(HC,1,400,1,30,0.2,10)
HC_water_pump.windows([480,510],[0,0],0.35)

HC_Fridge = HC.Appliance(HC,4,150,1,1440,0,30, 'yes',3)
HC_Fridge.windows([0,1440],[0,0])
HC_Fridge.specific_cycle_1(150,20,5,10)
HC_Fridge.specific_cycle_2(150,15,5,15)
HC_Fridge.specific_cycle_3(150,10,5,20)
HC_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

HC_microscope = HC.Appliance(HC,2,3,2,120,0.2,10)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(HC,3,3000,2,120,0.1,15)
HC_shower.windows([360,720],[780,1400],0.35)

HC_heater = HC.Appliance(HC,2,1500,2,180,0.25,60)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HC.Appliance(HC,2,500,2,60,0.15,10)
HC_dental_compresor.windows([480,720],[840,1260],0.2)

HC_centrifuge = HC.Appliance(HC,2,100,1,60,0.15,10)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(HC,2,10,1,60,0.25,15)
HC_serological_rotator.windows([480,720],[0,0],0.35)

#School B
SB_indoor_bulb = SB.Appliance(SB,12,7,2,120,0.25,30)
SB_indoor_bulb.windows([480,780],[840,1140],0.2)

SB_outdoor_bulb = SB.Appliance(SB,3,13,1,60,0.2,10)
SB_outdoor_bulb.windows([1007,1080],[0,0],0.35)

SB_TV = SB.Appliance(SB,1,60,2,120,0.1,5, occasional_use = 0.5)
SB_TV.windows([480,780],[840,1140],0.2)

SB_radio = SB.Appliance(SB,3,4,2,120,0.1,5, occasional_use = 0.5)
SB_radio.windows([480,780],[840,1140],0.2)

SB_DVD = SB.Appliance(SB,2,8,2,120,0.1,5, occasional_use = 0.5)
SB_DVD.windows([480,780],[840,1140],0.2)

SB_Freezer = SB.Appliance(SB,1,200,1,1440,0,30, 'yes',3)
SB_Freezer.windows([0,1440])
SB_Freezer.specific_cycle_1(200,20,5,10)
SB_Freezer.specific_cycle_2(200,15,5,15)
SB_Freezer.specific_cycle_3(200,10,5,20)
SB_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

SB_PC = SB.Appliance(SB,1,50,2,210,0.1,10)
SB_PC.windows([480,780],[840,1140],0.35)

SB_Phone_charger = SB.Appliance(SB,1,2,2,180,0.2,5)
SB_Phone_charger.windows([480,780],[840,1140],0.35)


#Public lighting
Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)

#Water supply system
WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)


#Grocery Store
GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_freezer.windows([0,1440],[0,0])
GS_freezer.specific_cycle_1(200,20,5,10)
GS_freezer.specific_cycle_2(200,15,5,15)
GS_freezer.specific_cycle_3(200,10,5,20)
GS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)



#Irrigation
IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)
