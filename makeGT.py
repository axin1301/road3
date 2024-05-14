from csv2txt_transform_new import transform_csv_to_txt_GT
from shapely.geometry import Point
import geopandas as gpd
import os

for year in [2019, 2017, 2021]:
    for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        if not os.path.exists('../temp_output/GraphSamplingToolkit-main/'+county+'_'+str(year)+'/groundtruth2/'+county+'_'+str(year)+'_edges_osm.txt'):
            transform_csv_to_txt_GT(year,county)

#####主要是生成GT，应该比较快