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
### Only IGA
#Defining users (14 users but with the school type B) and helath center instead of the helath post

GS = User("Grocery Store 1", 4)
User_list.append(GS)

IW = User("Irrigation Water", 15)
User_list.append(IW)

#Appliances

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