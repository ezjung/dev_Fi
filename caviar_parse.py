#! /usr/bin/env python3

import pandas as pd
import os, sys
# config file path append to call config.py
sys.path.append(os.path.abspath('/home/sung/Umami/scripts/Finance_Umami'))
from config import *

# Function which sort_index by ascending; only save the month of May; write week_of_day   
def refine(df):
    df.sort_index(ascending=True, inplace = True)
    df = df.loc[(df.index.year == year) & (df.index.month == month)]
    df['day'] = df.index.day_name()
    return df

# To use this func, df should have datetime convertible index
# Should be all numbers to use this program
def dfWithDateIndexNoDollar(df):
    df.index = pd.to_datetime(df.index)
    df = df.replace( '[\$,)]', '', regex=True ). \
        replace( '[(]', '-', regex=True)
    df = df.apply(pd.to_numeric, downcast='float', errors='ignore')
    return df

# read the scrap files under meta/caviar, change datetime and save in dfs list
dfs = []
col_names = ['serial', 'ID', 'Pickup time', 'Price', 'Tax', 'Fee', 'Umami portion']
for fname in os.listdir(
    os.chdir(
        os.path.join(
            path_shared, period, meta, caviar
        )
    )
):
    if fname.endswith('_scrap.csv'):
        df = pd.read_csv(fname, names = col_names)
        # df['Pickup time'] = pd.to_datetime(df['Pickup time']) # Will be assigned by dfWithDateIndexNoDollar
        df = df.set_index(['Pickup time']) # Time should be assigned as index here
        df = dfWithDateIndexNoDollar(df)
        dfs.append(df)

# For whole data; pd object need to be  saved in different name object
umami = pd.DataFrame()
for df in dfs:
    umami = umami.append(df)

# Make a copy of umami df
umami_df = umami.copy(deep=True)

# separate Diomnd (CUF) and Uptown (UPTOWN), and make new column
_, umami['Location'],_ = zip(*umami['ID'].str.split('-'))
# Remove '$' and all the values to float. to_numeric to avoid errors
umami = umami.drop(columns=['serial', 'ID']).replace('CUF', 'Dimond')
# groupby 'Location', total caviar data for sales tax calculation
grouped = umami.groupby('Location')
grp_calc = grouped.sum()

fname_caviar_calc = os.path.join(path_shared,period, report, period+'_'+'Umami_caviar_calculated.csv')
with open(fname_caviar_calc, 'w') as f:
    grp_calc.to_csv(f, header=True)

# paths = [path_shared, path]
# for pth in paths:
#     fname_caviar_calc = os.path.join(pth,period, report, period+'_'+'Umami_caviar_calculated.csv')
#     with open(fname_caviar_calc, 'w') as f:
#         grp_calc.to_csv(f, header=True)

# For night data; pd object need to be  saved in different name object
dfn = pd.DataFrame()
for df in dfs:
    dfNight = df.between_time('15:30', '22:00')
    dfn = dfn.append(dfNight)

# separate Diomnd (CUF) and Uptown (UPTOWN), and make new column
_, dfn['Location'],_ = zip(*dfn['ID'].str.split('-'))
# Remove '$' and all the values to float. to_numeric to avoid errors
dfn = dfn.drop(columns=['serial', 'ID']).replace('CUF', 'Dimond')
# groupby 'Location', total caviar data for sales tax calculation
grp_night = dfn.groupby('Location')
# split Dimond and Uptown night income
grp_list = [grp_night.get_group(x) for x in grp_night.groups]
# Dimond is grp_list[0] and Uptown is grp_list[1], no income yet!!
locs = ["Dimond", "Uptown"]
for Num, df in enumerate(grp_list):
    df = refine(df)
    # globals()[locs[Num]] = tipsCalc(globals()[lc])
    fname_night = os.path.join(path_shared, period, report, period + '_caviar' + '_' + locs[Num] + '_Night.csv')
    with open(fname_night, 'w') as f:
        df.to_csv(f, header=True)


    # paths = [path_shared, path]
    # for pth in paths:
    #     fname_night = os.path.join(pth, period, report, period + '_caviar' + '_' + locs[Num] + '_Night.csv')
    #     with open(fname_night, 'w') as f:
    #         df.to_csv(f, header=True)

# Umami Total caviar sales save to csv file under resport
umamiAll = refine(umami_df)

fname_umami = os.path.join(path_shared, period, report, period+'_'+'Umami_caviar.csv')
with open(fname_umami, 'w') as f:
    umamiAll.to_csv(f, header = True)

# paths = [path_shared, path]
# for pth in paths:
#     fname_umami = os.path.join(pth, period, report, period+'_'+'Umami_caviar.csv')
#     with open(fname_umami, 'w') as f:
#         umamiAll.to_csv(f, header = True)

