import os
from PIL import Image
import pandas as pd
import math
import numpy as np
import geopandas as gpd
import PIL.Image
import cv2
PIL.Image.MAX_IMAGE_PIXELS = None
import matplotlib.pyplot as plt
import glob
import shutil
from PIL import Image
import argparse

if not os.path.exists('../temp_output/cut_image/'):
    os.makedirs('../temp_output/cut_image/')

for district in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
    year = 2021
    img_temp=Image.open('../../RoadNetwork_Validation_final/temp_output/'+'topology_construction/'+district+'_GT_'+str(year)+'.png')
    # img_temp=Image.open('pred_skeleton_疏附县_2021_2.png')
    print(np.shape(img_temp))
    img_temp_cut = np.array(img_temp)[int(np.shape(img_temp)[0]/2)-2500 : int(np.shape(img_temp)[0]/2)+2500, int(np.shape(img_temp)[1]/2)-2500 : int(np.shape(img_temp)[1]/2)+2500]
    # plt.imshow(img_temp_cut)
    # plt.show()

    resized_img_tmp = Image.fromarray(img_temp_cut.astype(np.uint8))
    resized_img_tmp.save('../temp_output/cut_image/'+district+'_GT_primary_'+str(year)+'.png')
    # resized_img_tmp.save('./test_cut.png')