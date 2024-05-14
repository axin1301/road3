import os
from test import *
from RoadNetwortLable_by_each_road import *
from concat_all_label_image import *
from GT_post_processing import *
from shp2txt_transform import *
import sys  
sys.path.append('topology_construction') 
from topology_construction.transform_graph_main import *
from 
from mapcompare import *
from mapcompare_OSM import *
from mapcompare_d500_first_update_new0514 import *
import glob
import PIL
from PIL import Image
import pandas as pd
import numpy as np
PIL.Image.MAX_IMAGE_PIXELS = None
import datetime

def main():
    print("Hello World")
    with open("time_log_first10cts_update2021_geobias2.txt","w") as log_f:
        # for year in [2017,2021]:
        for year in [2019,2017,2021]:
            for up_para in [300]:
                for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
                # for county in ['xixiangxian']:
                    if os.path.exists('../output_update/'+county+'_'+str(year)+'_d500_'+str(up_para)+'_new3.csv'):
                        continue
                    # if os.path.exists('../../RoadNetwork_Validation_final/temp_output/GraphSamplingToolkit-main/xixiangxian_2017/groundtruth/xixiangxian_2017_edges_osm.txt'):
                    #                 #   /../../../../ \
                                    #   RoadNetwork_Validation_final/temp_output/GraphSamplingToolkit-main/xixiangxian_2017/groundtruth/xixiangxian_2017_vertices_osm.txt'):
                    #     print('True!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    mapcompare_d500_first_update_new('../temp_output_d500/GraphSamplingToolkit-main_improve5',county, 'xyx', 'LCR', year, up_para)
                    # mapcompare_d500('../temp_output_d500/GraphSamplingToolkit-main_update',county, 'xyx', 'LCR', year, up_para)
                # now_time = datetime.datetime.now()
                # log_f.write(county+'   ' +str(year) +'  '+'mapcompare'+ '  '+str(now_time))
                # log_f.write('\n')


        # year_list1 = []
        # county_list1 = []
        # positive_pixel_list = []
        # image_weight_list = []
        # image_height_list = []


        # for year in [2017,2021]:
        #     for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        #         img = Image.open('../temp_output/'+'topology_construction/'+county+'_GT_'+str(year)+'.png')
        #         img_np = np.array(img)
        #         pos_idx = np.where(img_np>0)
        #         year_list1.append(year)
        #         county_list1.append(county)
        #         positive_pixel_list.append(len(pos_idx[0]))
        #         image_weight_list.append(img_np.shape[0])
        #         image_height_list.append(img_np.shape[1])
        #         now_time = datetime.datetime.now()
        #         log_f.write(county +  '   ' +str(year) +'  '+'GT_statistics'+ '  '+str(now_time))
        #         log_f.write('\n')
        
        # pd_statis = pd.DataFrame({'county':county_list1, 'year':year_list1,'pos_pixel':positive_pixel_list, \
        #                           'img_weight':image_weight_list,'img_height':image_height_list})
        # pd_statis.to_csv('GT_statistics.csv', index=False)

        for up_para in [300]:
            # for year in [2017,2021]:
            for year in [2019,2017,2021]:
                df_all = pd.DataFrame({})
                for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
                    df = pd.read_csv('../output_update/'+county+'_'+str(year)+'_d500_'+str(up_para)+'_new3.csv')
                    df_all = pd.concat([df_all, df])
                    # now_time = datetime.datetime.now()
                    # log_f.write(county +  '   ' +str(year) +'  '+'validation_statistics_all'+ '  '+str(now_time))
                    # log_f.write('\n')

                df_all.to_csv('validation_statistics_all_first10cts_d500_'+str(year)+'_'+str(up_para)+'_new3.csv', index=False)


    # with open("time_log_first10cts_OSM.txt","w") as log_f:
    #     for year in [2018,2022]:
    #         for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
    #             mapcompare_OSM('../temp_output_OSM/GraphSamplingToolkit-main',county, 'xyx', 'LCR', year)
    #             # now_time = datetime.datetime.now()
    #             # log_f.write(county+'   ' +str(year) +'  '+'mapcompare'+ '  '+str(now_time))
    #             # log_f.write('\n')


    #     # year_list1 = []
    #     # county_list1 = []
    #     # positive_pixel_list = []
    #     # image_weight_list = []
    #     # image_height_list = []


        # # for year in [2017,2021]:
        # #     for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        # #         img = Image.open('../temp_output/'+'topology_construction/'+county+'_GT_'+str(year)+'.png')
        # #         img_np = np.array(img)
        # #         pos_idx = np.where(img_np>0)
        # #         year_list1.append(year)
        # #         county_list1.append(county)
        # #         positive_pixel_list.append(len(pos_idx[0]))
        # #         image_weight_list.append(img_np.shape[0])
        # #         image_height_list.append(img_np.shape[1])
        # #         now_time = datetime.datetime.now()
        # #         log_f.write(county +  '   ' +str(year) +'  '+'GT_statistics'+ '  '+str(now_time))
        # #         log_f.write('\n')
        
        # # pd_statis = pd.DataFrame({'county':county_list1, 'year':year_list1,'pos_pixel':positive_pixel_list, \
        # #                           'img_weight':image_weight_list,'img_height':image_height_list})
        # # pd_statis.to_csv('GT_statistics.csv', index=False)

        # df_all = pd.DataFrame({})
        # for year in [2018,2022]:
        #     for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        #         df = pd.read_csv('../output/'+county+'_'+str(year)+'_OSM.csv')
        #         df_all = pd.concat([df_all, df])
        #         now_time = datetime.datetime.now()
        #         log_f.write(county +  '   ' +str(year) +'  '+'validation_statistics_all_OSM'+ '  '+str(now_time))
        #         log_f.write('\n')

        # df_all.to_csv('validation_statistics_all_first10cts_OSM.csv', index=False)

    # for year in [2017,2021]:
    #     for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
    #     # data = gpd.read_file(county+'/edges.shp')

    #         data= gpd.read_file('../../RoadNetwork_Validation_final/data/tdrive_sample/results_GT_'+ county +'_'+str(year)+'/extracted_rn/edges.shp')
    #         data.crs = "EPSG:4326"
    #         data.to_crs("EPSG:32650",inplace=True)
    #         # print(data.crs)
    #         data['distance'] = data.geometry.length
    #         # print(data.head())

    #         distance_list = list(data['distance'])
    #         # print(max(distance_list))
    #         # print(min(distance_list))

    #         score = pd.Series(distance_list)
    #         se1 = pd.cut(score, [0,50,100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,100000]) # 统计0-1,1-2依次类推各个区间的数值数量
    #         df = gpd.read_file('../../RoadNetwork_Validation_final/data/tdrive_sample/results_GT_'+ county +'_'+str(year)+'/extracted_rn/nodes.shp')
    #         print(county, year, len(df))
    #         print(list(se1.value_counts()))
    #         # x_list.append(list(se1.value_counts()))



if __name__=="__main__":
    main()