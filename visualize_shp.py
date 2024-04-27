import geopandas as gpd
import matplotlib.pyplot as plt

for county in ['jingyuxian','liboxian','shufuxian']:
    for year in [2021]:
        
        geo_df1 = gpd.read_file('../data/tdrive_sample/results_GT_'+county+'_'+str(year)+'/extracted_rn/edges.shp')

        # 绘制地图
        geo_df1.plot()
        plt.savefig('GT_'+county+'_'+str(year)+'.png')  # 保存地图为 PNG 图片
        plt.show()
    
        # 关闭之前的图形
        plt.close()
