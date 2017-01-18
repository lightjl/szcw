# 1.发展指标
#    主营业务收入（ operating_revenue ）增长率
#    主营业务收入增长的含金量
#    净利润 net_profit
# 2.控制能力--成本控制


# 5.偿还能力
# 资产负债率,流动比率,速动比率

import time
from datetime import date
from datetime import datetime, timedelta
import pandas as pd

watch_list = ['002078.XSHE', '002372.XSHE', '600522.XSHG', '000501.XSHE', '600176.XSHG', '601009.XSHG', '600373.XSHG', '600066.XSHG']
all_stcok = get_all_securities(['stock'])
now = datetime.now()
year_now = now.year

q = query(
    income.code, income.operating_revenue, income.net_profit
).filter(
    valuation.code.in_(watch_list)
)
year_watch = [year_now -1-i for i in range(5)]   # 2016 2015 2014
df1 = [get_fundamentals(q, statDate=year_watch[i]) for i in range(5)]

check_list = []
y_danwei = 100000000
for i in watch_list:
    #operating_revenue
    tmp_list = []
    df_check = df1[0][df1[0].code==i]
    tmp_list.extend([i, all_stcok.ix[i].display_name.replace(' ', ''), u'主营业务收入'])
    if df1[0][df1[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ round(df_check['operating_revenue'].values[0]/y_danwei,3) ])

    for j in range(1,5):
        df_check = df1[j][df1[j].code==i]
        tmp_list.extend([round(df_check['operating_revenue'].values[0]/y_danwei,3)])

    # net_profit
    df_check = df1[0][df1[0].code==i]
    tmp_list.extend([u'净利润'])
    if df1[0][df1[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ round(df_check['net_profit'].values[0]/y_danwei,3) ])
    for j in range(1,5):
        df_check = df1[j][df1[j].code==i]
        tmp_list.extend([round(df_check['net_profit'].values[0]/y_danwei,3)])
    check_list.append(tmp_list)

    # calculate growth rate
    tmp_list2 = []
    tmp_list2.extend([i, all_stcok.ix[i].display_name.replace(' ', ''),u'主营growth'])
    for j in range(3,7):
        if tmp_list[j] == 0:
            tmp_list2.extend([0])
            continue
        tmp_list2.extend([str(round((tmp_list[j] - tmp_list[j+1])/tmp_list[j+1]*100,2))+'%'])
    tmp_list2.extend([0])
    
    tmp_list2.extend([u'净growth'])
    for j in range(9,13):
        if tmp_list[j] == 0:
            tmp_list2.extend([0])
            continue
        tmp_list2.extend([str(round((tmp_list[j] - tmp_list[j+1])/tmp_list[j+1]*100,2))+'%'])
    tmp_list2.extend([0])
    check_list.append(tmp_list2)

# columns=[u'code', u'名称'] + [str(year_watch[i]-2000) for i in range(5)]+ [str(year_watch[i]-2000) for i in range(5)]
columns=[u'code', u'名称', u'yw'] + ['%s'  %(str(year_watch[i]-2000) ) for i in range(5) ] + [u'yw']  + ['%s'  %(str(year_watch[i]-2000) ) for i in range(5) ]



df_watch= pd.DataFrame(data=check_list, columns=columns)
df_watch
