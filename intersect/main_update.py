import os
from construct_node_shp import *
from cal_dif_update import *
from statis_update import *
# from tmp import *

# tmp()
# tmp2()
# construct_node_shp()
# cal_dif()
# statis()
os.makedirs('./results_update')
cal_dif()
statis()

# os.system('construct_node_shp.py')
# os.system('cal_dif.py')
# os.system('statis.py')