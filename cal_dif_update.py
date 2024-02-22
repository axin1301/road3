import geopandas as gpd
import pandas as pd
import os

# Function to find the nearest point in gdf_B for each point in gdf_A
def find_nearest(point, gdf_to):
    nearest_id = gdf_to.geometry.distance(point).idxmin()
    distance = gdf_to.geometry.distance(point).min()
    return pd.Series([nearest_id, distance], index=['nearest_point_id', 'distance'])

def output_df(gdf_GT_OSM,gdf_OSM,district,year,typee):
        # Apply the function to gdf_A to find the nearest points and distances from gdf_B
        nearest_info = gdf_GT_OSM['geometry'].apply(find_nearest, gdf_to=gdf_OSM)
        # Concatenate the nearest info with gdf_A
        gdf_GT_OSM = pd.concat([gdf_GT_OSM, nearest_info], axis=1)
        # Sort gdf_A by distance
        gdf_GT_OSM = gdf_GT_OSM.sort_values(by='distance')
        # Remove duplicates based on the nearest_point_id column, keeping the first occurrence
        gdf_GT_OSM = gdf_GT_OSM.drop_duplicates(subset='nearest_point_id', keep='first')
        # Save the resulting GeoDataFrame to a new shapefile
        gdf_GT_OSM.to_file('results_update/'+district+'_'+str(year)+'_'+typee+'.shp')
        

def cal_dif():
    for year in [2017,2021]:
        for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
            # #读取两个 shapefile 文件
            # # if not os.path.exists('b2/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp'):
            # #     continue
            # # gdf_OSM = gpd.read_file('OSM/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # gdf_pred = gpd.read_file('pred_update/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # # gdf_b1 = gpd.read_file('b1/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # # gdf_b2 = gpd.read_file('b2/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # # gdf_GT_OSM = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # gdf_GT_pred = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # # gdf_GT_b1 = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')
            # # gdf_GT_b2 = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_2.shp')

            # # output_df(gdf_GT_OSM,gdf_OSM,county,year,'OSM_2')
            # output_df(gdf_GT_pred,gdf_pred,county,year,'pred_2')
            # # output_df(gdf_GT_b1,gdf_b1,county,year,'b1_2')
            # # output_df(gdf_GT_b2,gdf_b2,county,year,'b2_2')

            if os.path.exists('results_update/'+county+'_'+str(year)+'_'+'pred_3'+'.shp'):
                continue

            # gdf_OSM = gpd.read_file('OSM/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            gdf_pred = gpd.read_file('pred_update/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            # gdf_b1 = gpd.read_file('b1/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            # gdf_b2 = gpd.read_file('b2/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            # gdf_GT_OSM = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            gdf_GT_pred = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            # gdf_GT_b1 = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')
            # gdf_GT_b2 = gpd.read_file('GT/'+county+'_'+str(year)+'_nodes_degree_gt_3.shp')

            # output_df(gdf_GT_OSM,gdf_OSM,county,year,'OSM_3')
            output_df(gdf_GT_pred,gdf_pred,county,year,'pred_3')
            # output_df(gdf_GT_b1,gdf_b1,county,year,'b1_3')
            # output_df(gdf_GT_b2,gdf_b2,county,year,'b2_3')


