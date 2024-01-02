import os
os.chdir("./Orbit_Planets/")

from ursina import *
import numpy as np
from utils import calcfuns

#%%

app = Ursina()

sun = Entity(model='quad',
           texture="./textures/sun.png", 
           scale = 2)

earth = Entity(model='quad',
           texture="./textures/earth.png", 
           scale = .7)

#Get constants
planets = calcfuns.setconstants()

x_orb,y_orb,z_orb    = 1.0167*planets['Au']  ,0,0
xv_orb,yv_orb,zv_orb = 0,planets['e_ap_v'],0

x_sun,y_sun,z_sun    = 0,0,0
xv_sun,yv_sun,zv_sun = 0,0,0
timeNum           = 0.0

radEarth = 3

def update():
    global x_orb, y_orb, z_orb, x_sun, y_sun, z_sun, xv_orb, yv_orb, zv_orb, xv_sun, yv_sun, zv_sun, timeNum
    global radEarth
    
    x_orb, y_orb, z_orb,x_sun, y_sun, z_sun,xv_orb, yv_orb, zv_orb,xv_sun, yv_sun, zv_sun, timeNum = calcfuns.calcposition(x_orb, y_orb, z_orb, 
                                        x_sun, y_sun, z_sun,
                                        xv_orb, yv_orb, zv_orb, 
                                        xv_sun, yv_sun, zv_sun,
                                        timeNum)
    earth.x = x_orb / planets['Au'] * radEarth
    earth.y = y_orb / planets['Au'] * radEarth
    earth.z = z_orb / planets['Au'] * radEarth
    
    sun.x = x_sun / planets['Au']
    sun.y = y_sun / planets['Au']
    sun.z = z_sun / planets['Au']

app.run()
