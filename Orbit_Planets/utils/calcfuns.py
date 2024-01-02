

def setconstants():
    # constants
    # https://archive.is/9ZT5e#selection-979.0-1003.19
    planets = {}
    planets['G']           = 6.67e-11           # constant G
    planets['Msun']          = 2.0e30             # sun
    planets['Mearth']          = 5.972e24           # earth        
    planets['Au']          = 1.5e11
    planets['daysec']      = 24.0*60*60         # seconds of a day
    planets['e_ap_v']      = 29290              # earth velocity at aphelion
    planets['gravconst_e'] = planets['G'] * planets['Mearth'] *  planets['Msun'] 
    
    return planets

def calcposition(x_orb, y_orb, z_orb, 
                x_sun, y_sun, z_sun,
                xv_orb, yv_orb, zv_orb, 
                xv_sun, yv_sun, zv_sun,
                timeNum):
    
    planets = setconstants()
    gravconst_e = planets['gravconst_e']
    Morb = planets['Mearth']
    Msun = planets['Msun']
    dt = 1*planets['daysec'] 
    
    rx,ry,rz = x_orb - x_sun, y_orb - y_sun, z_orb - z_sun
    modr3_e = (rx**2+ry**2+rz**2)**1.5
    fx_e = -gravconst_e*rx/modr3_e
    fy_e = -gravconst_e*ry/modr3_e
    fz_e = -gravconst_e*rz/modr3_e
    
    xv_orb += fx_e*dt/Morb
    yv_orb += fy_e*dt/Morb
    zv_orb += fz_e*dt/Morb
    
    x_orb += xv_orb*dt - x_sun
    y_orb += yv_orb*dt - y_sun
    z_orb += zv_orb*dt - z_sun
            
    xv_sun += -fx_e*dt/Msun
    yv_sun += -fy_e*dt/Msun
    zv_sun += -fz_e*dt/Msun
    
    x_sun += xv_sun*dt
    y_sun += yv_sun*dt 
    z_sun += zv_sun*dt
    
    timeNum +=dt
    
    return x_orb, y_orb, z_orb, x_sun, y_sun, z_sun, xv_orb, yv_orb, zv_orb, xv_sun, yv_sun, zv_sun, timeNum