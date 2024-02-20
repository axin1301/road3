import pandas as pd
import os

for year in [2017,2021]:
    if year == 2017:
        up_para = 100
    elif year == 2021:
        up_para = 300
    for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        for token in ['d500']:
            df_all = pd.DataFrame({})
            for roadclass in [49,41000,42000,44000,45000,47000,51000,52000,53000,54000]:
                if os.path.exists('../output/'+county+'_'+str(year)+'_'+str(roadclass)+'_'+token+'_'+str(up_para)+'_recall.csv'):
                    print('../output/'+county+'_'+str(year)+'_'+str(roadclass)+'_'+token+'_'+str(up_para)+'_recall.csv')
                    df = pd.read_csv('../output/'+county+'_'+str(year)+'_'+str(roadclass)+'_'+token+'_'+str(up_para)+'_recall.csv')
                    df_all = pd.concat([df_all, df])
            df_all.to_csv('../output/'+county+'_'+str(year)+'_'+token+'_'+str(up_para)+'_recall.csv', index=False)



df_all = pd.DataFrame({})
for year in [2017]:
    for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_d500_100_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_d500_100_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_2017_first10_d500_100_recall.csv', index=False)


data = pd.read_csv('validation_statistics_2017_first10_d500_100_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_2017_first10_d500_100_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名

##############################################################################

df_all = pd.DataFrame({})
for year in [2021]:
    for county in ['xixiangxian','shufuxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian','linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_d500_300_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_d500_300_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_2021_first10_d500_300_recall.csv', index=False)


data = pd.read_csv('validation_statistics_2021_first10_d500_300_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_2021_first10_d500_300_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名