import os
from Preprocessing import *

VorW = "wolf_win"
path_list = os.listdir(VorW)

for path in path_list:
    name = path[:-4]
    Preprocessing(name, VorW)
    print( path + "-> end")
