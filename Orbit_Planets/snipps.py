#%%
import os
os.chdir("./Orbit_Planets/")

from utils import calcfuns
import numpy as np
import matplotlib.pyplot as plt


#%%

planets = calcfuns.setconstants()

#%%

x_orb, y_orb, z_orb = 1.0167*planets['Au']  ,0,0
xv_orb, yv_orb, zv_orb = 0,planets['e_ap_v'] ,0

x_sun, y_sun, z_sun   = 0,0,0
xv_sun, yv_sun, zv_sun = 0,0,0

# %%

x_orbL = np.zeros((365))
y_orbL = np.zeros((365))
z_orbL = np.zeros((365))

time = 0.0

for ii in range(len(x_orbL)):
    x_orb, y_orb, z_orb, x_sun, y_sun, z_sun, xv_orb, yv_orb, zv_orb, xv_sun, yv_sun, zv_sun, time = calcfuns.calcposition(x_orb, y_orb, z_orb, 
                    x_sun, y_sun, z_sun,
                    xv_orb, yv_orb, zv_orb, 
                    xv_sun, yv_sun, zv_sun,
                    time)

    x_orbL[ii] =  x_orb
    y_orbL[ii] =  y_orb
    z_orbL[ii] =  z_orb

# %%

plt.plot(x_orbL, y_orbL)

# %%
