import geopandas as gpd
import pandas as pd
import os

def statis():
    # year_list = []
    # county_list = []
    # GT_len_list = []
    # match0001_list = []
    # match005_list = []
    # match001_list = []
    # match05_list = []
    # match01_list = []

    # for year in [2017,2021]:
    #     for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
    #         # if not os.path.exists('b2/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp'):
    #         #     continue
    #         gdf_A = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
    #         gdf_C = gpd.read_file('results_update/'+county+'_'+str(year)+'_'+'pred_2'+'.shp')
    #         year_list.append(year)
    #         county_list.append(county)
    #         GT_len_list.append(len(gdf_A))
    #         # for thresh in [0.0001,0.005,0.001,0.05,0.01]:
    #         tmp_list = [x for x in list(gdf_C['distance']) if x < 0.0001]
    #             # print(thresh, len(tmp_list)/len((gdf_A)))
    #         match0001_list.append(float(len(tmp_list)/len(gdf_A)))
    #         tmp_list = [x for x in list(gdf_C['distance']) if x < 0.005]
    #         match005_list.append(float(len(tmp_list)/len(gdf_A)))
    #         tmp_list = [x for x in list(gdf_C['distance']) if x < 0.001]
    #         match001_list.append(float(len(tmp_list)/len(gdf_A)))
    #         tmp_list = [x for x in list(gdf_C['distance']) if x < 0.05]
    #         match05_list.append(float(len(tmp_list)/len(gdf_A)))
    #         tmp_list = [x for x in list(gdf_C['distance']) if x < 0.01]
    #         match01_list.append(float(len(tmp_list)/len(gdf_A)))

    # pd_dict = pd.DataFrame({'year':year_list,'county':county_list,'GT_len':GT_len_list,'m0001':match0001_list,'m005':match005_list, \
    #                         'm001':match001_list,'m05':match05_list,'m01':match01_list})
    # pd_dict.to_csv('first10_intersec_2_update.csv', index=False)



    year_list = []
    county_list = []
    GT_len_list = []
    match0001_list = []
    match005_list = []
    match001_list = []
    match05_list = []
    match01_list = []

    for year in [2017,2021]:
        for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
            # if not os.path.exists('b2/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp'):
            #     continue
            gdf_A = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            gdf_C = gpd.read_file('results_update/'+county+'_'+str(year)+'_'+'pred_3'+'.shp')
            year_list.append(year)
            county_list.append(county)
            GT_len_list.append(len(gdf_A))
            # for thresh in [0.0001,0.005,0.001,0.05,0.01]:
            tmp_list = [x for x in list(gdf_C['distance']) if x < 0.0001]
                # print(thresh, len(tmp_list)/len((gdf_A)))
            match0001_list.append(float(len(tmp_list)/len(gdf_A)))
            tmp_list = [x for x in list(gdf_C['distance']) if x < 0.005]
            match005_list.append(float(len(tmp_list)/len(gdf_A)))
            tmp_list = [x for x in list(gdf_C['distance']) if x < 0.001]
            match001_list.append(float(len(tmp_list)/len(gdf_A)))
            tmp_list = [x for x in list(gdf_C['distance']) if x < 0.05]
            match05_list.append(float(len(tmp_list)/len(gdf_A)))
            tmp_list = [x for x in list(gdf_C['distance']) if x < 0.01]
            match01_list.append(float(len(tmp_list)/len(gdf_A)))

    pd_dict = pd.DataFrame({'year':year_list,'county':county_list,'GT_len':GT_len_list,'m0001':match0001_list,'m005':match005_list, \
                            'm001':match001_list,'m05':match05_list,'m01':match01_list})
    pd_dict.to_csv('first10_intersec_3_update.csv', index=False)