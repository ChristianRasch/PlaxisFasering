# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:17:40 2018

@author: c.rasch
"""

import sys

localhostport_input = 10000
localhostport_output = 10001

#plaxis_path = r'C:\Program Files\Plaxis\PLAXIS 2D 201701'
##plaxis_path = r'C:\Program Files\Plaxis\PLAXIS 2D 2018.00'

sys.path.append(r'C:\Program Files\Plaxis\PLAXIS 2D 201701\python\Lib\site-packages')

from plxscripting.easy import *

wachtwoord = 'D<V3e#Fv/Dv5cv$V' # PLAXIS 2018

s_o, g_o = new_server('localhost', localhostport_output,password=wachtwoord)
s_i, g_i = new_server('localhost', localhostport_input,password=wachtwoord)


from mss import mss
import mss.tools
import time
import pyautogui
import numpy as np
from tkinter import *

def fromPositionL():
        
    input("Plaats de muis linksboven ")
    return pyautogui.position() 

def fromPositionR():
        
    input("Plaats de muis rechtsonder ")
    return pyautogui.position() 


pos1 = fromPositionL()
pos2 = fromPositionR()

x0 = pos1[0]
y0 = pos1[1]

width = np.abs(pos2[0]-pos1[0])
height = np.abs(pos1[1]-pos2[1])


for fase in g_i.Phases[:]:

    g_i.setcurrentphase(fase)
    
    time.sleep(2)
    
    print(fase.Identification.value)
    
    naam = fase.Identification.value
    
    with mss.mss() as sct:
    # The screen part to capture
#        monitor = {"top": 200, "left": 500, "width": 1300, "height": 650}
        monitor = {"top": int(y0), "left": int(x0), "width": int(width), "height": int(height)}
        output = str(naam + ".png".format(**monitor))
    
        # Grab the data
        sct_img = sct.grab(monitor)
    
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


    
    
    
