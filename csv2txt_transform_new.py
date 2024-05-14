import os
from PIL import Image
import numpy as np
import geopandas as gpd
import PIL.Image
import cv2
PIL.Image.MAX_IMAGE_PIXELS = None
import matplotlib.pyplot as plt
import glob
import pandas as pd
import math
import scipy.io as scio
from shapely.geometry import Polygon
from shapely.geometry import Point
import numpy as np
import math
#import geopandas
#import osmnx as ox
import urllib
import json
import argparse

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


class Geocoding:
    def __init__(self, api_key):
        self.api_key = api_key

    def geocode(self, address):
        """
        利用高德geocoding服务解析地址获取位置坐标
        :param address:需要解析的地址
        :return:
        """
        geocoding = {'s': 'rsv3',
                     'key': self.api_key,
                     'city': '全国',
                     'address': address}
        geocoding = urllib.urlencode(geocoding)
        ret = urllib.urlopen("%s?%s" % ("http://restapi.amap.com/v3/geocode/geo", geocoding))

        if ret.getcode() == 200:
            res = ret.read()
            json_obj = json.loads(res)
            if json_obj['status'] == '1' and int(json_obj['count']) >= 1:
                geocodes = json_obj['geocodes'][0]
                lng = float(geocodes.get('location').split(',')[0])
                lat = float(geocodes.get('location').split(',')[1])
                return [lng, lat]
            else:
                return None
        else:
            return None


def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

def transform_csv_to_txt_GT(year,district):

    if not os.path.exists('../temp_output/GraphSamplingToolkit-main/'+district+'_'+str(year)+'/groundtruth2/'): #2表示从csv直接得到的GT
        os.makedirs('../temp_output/GraphSamplingToolkit-main/'+district+'_'+str(year)+'/groundtruth2/')

    df = pd.read_csv('../data/district_boundary_long_lat3.csv')
    district_cn = list(df[df['latin']==district]['district'])[0]
    dt_code_cn = list(df[df['latin']==district]['dt_code'])[0]
    pd_dict_GT = pd.read_csv('../data/tilefile_zl16_20_plus_20/'+ district_cn+'.csv')

    # xiaoxian_road_GT_file = 'driving_road_xiaoxian_0_2020.geojson'
    # osm_road = gpd.read_file(xiaoxian_road_GT_file)

    district_road_GT_file = '../data/GT_GaoDe.csv' ############
    osm_road_full = pd.read_csv(district_road_GT_file)
    osm_road = osm_road_full[(osm_road_full['dt_code']==dt_code_cn) & (osm_road_full['year']==year)]
    osm_road.reset_index(inplace=True)
    print(len(osm_road))
    print(osm_road)

    district_bound = gpd.read_file('../district_bound/'+district_cn+'.geojson')

#######将县和年份对应的路网提取
    with open('../temp_output/GraphSamplingToolkit-main/'+district+'_'+str(year)+'/groundtruth2/'+district+'_'+str(year)+'_vertices_osm.txt', 'w') as f_points:
        point_dict = {}  # 用于存储点的经纬度和对应的编号
        point_id = 1
        with open('../temp_output/GraphSamplingToolkit-main/'+district+'_'+str(year)+'/groundtruth2/'+district+'_'+str(year)+'_edges_osm.txt', 'w') as f_connections:
            line_number = 1  # 行号
            for road_idx in range(len(osm_road)): ###################original geojson
                geo1 = osm_road.at[road_idx,'link_coors']  #每一条路先制成一个label， geometry为一个lon,lat list
                #####geo1 此时为一个字符串list 类似于 116.396574,34.639533;116.396547,34.639399;116.396676,34.638675;116.396703,34.638433
                road_name = osm_road.at[road_idx,'id'] ##希望每条路可以有一个标号,类似于一个unique id,如果没有,我再修改一下.. 
                # if road_name!=225534870:
                #     continue
                print(road_name)
                
                # geo1= list(geo1.geoms)
                # point_list = []
                p1_list = []
                p2_list = []
                p1_list_all = []
                p2_list_all = []
                for g in list(geo1.split(';')):
                    lng_gcj = float(g.split(',')[0])
                    lat_gcj = float(g.split(',')[1])
                    lng_wgs, lat_wgs = gcj02_to_wgs84(lng_gcj,lat_gcj)
                    point = Point(lng_wgs, lat_wgs)
                    p1_list_all.append(lat_wgs)
                    p2_list_all.append(lng_wgs)

                    if district_bound.geometry.iloc[0].contains(point):
                        # print('contain')
                        p1_list.append(lat_wgs)
                        p2_list.append(lng_wgs)

                    # point_list.append(g)

                for coord_idx in range(len(p1_list)):
                    coord_str = f"{p2_list[coord_idx]},{p1_list[coord_idx]}"  # 将经纬度转换为字符串
                    if coord_str not in point_dict:
                        point_dict[coord_str] = point_id
                        f_points.write(f"{point_id},{p2_list[coord_idx]},{p1_list[coord_idx]}\n")
                        point_id += 1

            # 判断点之间是否相连，并写入连接关系的文本文件
                for coord_idx in range(len(p1_list_all)-1):    
                        coord1_str = f"{p2_list_all[coord_idx]},{p1_list_all[coord_idx]}"
                        coord2_str = f"{p2_list_all[coord_idx+1]},{p1_list_all[coord_idx+1]}"
                        if coord1_str in point_dict and coord2_str in point_dict:
                            point_id1 = point_dict[coord1_str]
                            point_id2 = point_dict[coord2_str]
                            f_connections.write(f"{line_number},{point_id1},{point_id2},1\n")
                            line_number += 1