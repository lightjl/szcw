# 3.营运能力
# 人、物、财的运用效率
# 周转率和效率
# 应收账款周转率=income.operating_revenue/(balance.account_receivable	应收账款(元))/2
# 存货周转率=income.operating_cost	营业成本(元)/balance.inventories 平均存货
# 货币资金的管理
# 固定资产的营运效率=income.operating_revenue/balance.fixed_assets 固定资产
# 总资产的营运效率 total_sheet_owner_equities 负债和股东权益合计=资产总额
# =income.operating_revenue/balance.total_sheet_owner_equities

import time
from datetime import date
from datetime import datetime, timedelta
import pandas as pd

watch_list = ['002078.XSHE', '002372.XSHE', '600522.XSHG', '000501.XSHE', '600176.XSHG', '601009.XSHG', '600373.XSHG', '600066.XSHG']
#watch_list = ['601009.XSHG']
watch_list = get_industry_stocks('C22')
#'C22'
#'C29'
#'C38'
#'HY467'
#'C30'
#'J66'
#'R85'
#'C36'




all_stcok = get_all_securities(['stock'])
now = datetime.now()
year_now = now.year

q = query(
    income.code, income.operating_revenue, balance.account_receivable,
    income.operating_cost, balance.inventories, balance.fixed_assets,
    balance.total_sheet_owner_equities
).filter(
    valuation.code.in_(watch_list)
)
year_watch = [year_now -1-i for i in range(3)]   # 2016 2015 2014
df3 = [get_fundamentals(q, statDate=year_watch[i]) for i in range(3)]

check_list = []
for i in watch_list:
    tmp_list = []
    df_check = df3[0][df3[0].code==i]
    df_before = df3[1][df3[1].code==i]
    tmp_list.extend([i, all_stcok.ix[i].display_name.replace(' ','')])
    # 应收账款周转率
    if df3[0][df3[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([round(df_check['operating_revenue']/\
                 (df_check['account_receivable']+df_before['account_receivable'])*2,2)])
    df_check = df3[1][df3[1].code==i]
    df_before = df3[2][df3[2].code==i]
    tmp_list.extend([round(df_check['operating_revenue']/\
        (df_check['account_receivable']+df_before['account_receivable'])*2,2)])

    # 存货周转率
    df_check = df3[0][df3[0].code==i]
    df_before = df3[1][df3[1].code==i]
    if df3[0][df3[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([round(df_check['operating_cost']/\
                 (df_check['inventories']+df_before['inventories'])*2,2)])
    df_check = df3[1][df3[1].code==i]
    df_before = df3[2][df3[2].code==i]
    tmp_list.extend([round(df_check['operating_cost']/\
                 (df_check['inventories']+df_before['inventories'])*2,2)])

    # 固定资产周转率
    df_check = df3[0][df3[0].code==i]
    df_before = df3[1][df3[1].code==i]
    if df3[0][df3[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([round(df_check['operating_revenue']/\
                 (df_check['fixed_assets']+df_before['fixed_assets'])*2,2)])
    df_check = df3[1][df3[1].code==i]
    df_before = df3[2][df3[2].code==i]
    tmp_list.extend([round(df_check['operating_revenue']/\
                 (df_check['fixed_assets']+df_before['fixed_assets'])*2,2)])

    # 总资产周转率
    df_check = df3[0][df3[0].code==i]
    df_before = df3[1][df3[1].code==i]
    if df3[0][df3[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([round(df_check['operating_revenue']/\
                 (df_check['total_sheet_owner_equities']+df_before['total_sheet_owner_equities'])*2,2)])
    df_check = df3[1][df3[1].code==i]
    df_before = df3[2][df3[2].code==i]
    tmp_list.extend([round(df_check['operating_revenue']/\
                 (df_check['total_sheet_owner_equities']+df_before['total_sheet_owner_equities'])*2,2)])
    check_list.append(tmp_list)
columns = [u'code', u'name', u'16yszk', u'15yszk', u'16ch', u'15ch', u'16gd', u'15gd', u'16zzc', u'15zzc']
df_watch3=pd.DataFrame(data=check_list,columns=columns)
df_watch3
