# 4.盈利能力
# 毛利率,净利润率,净资产收益率ROE indicator
# gross_profit_margin	销售毛利率(%)
# net_profit_to_total_revenue	净利润/营业总收入(%)
# operating_expense_to_total_revenue	营业费用/营业总收入(%)
# ga_expense_to_total_revenue	管理费用/营业总收入(%)
# financing_expense_to_total_revenue	财务费用/营业总收入(%)
# roe	净资产收益率ROE

import time
from datetime import date
from datetime import datetime, timedelta
import pandas as pd

watch_list = ['002078.XSHE', '002372.XSHE', '600522.XSHG', '000501.XSHE', '600176.XSHG', '601009.XSHG', '600373.XSHG', '600066.XSHG']
all_stcok = get_all_securities(['stock'])
now = datetime.now()
year_now = now.year

q = query(
    indicator.code, indicator.gross_profit_margin, indicator.net_profit_to_total_revenue,
    indicator.operating_expense_to_total_revenue, indicator.ga_expense_to_total_revenue,
    indicator.financing_expense_to_total_revenue, indicator.roe
).filter(
    valuation.code.in_(watch_list)
)
year_watch = [year_now -1-i for i in range(5)]   # 2016 2015 2014
df4 = [get_fundamentals(q, statDate=year_watch[i]) for i in range(5)]

check_list = []
y_danwei = 100000000
for i in watch_list:
    # gross_profit_margin   销售毛利率(%)
    tmp_list = []
    df_check = df4[0][df4[0].code==i]
    tmp_list.extend([i, all_stcok.ix[i].display_name.replace(' ', ''), u'毛利率'])
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['gross_profit_margin'].values[0] ])

    for j in range(1,5):
        df_check = df4[j][df4[j].code==i]
        tmp_list.extend([ df_check['gross_profit_margin'].values[0] ])

    # net_profit_to_total_revenue 净利润/营业总收入(%)
    df_check = df4[0][df4[0].code==i]
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['net_profit_to_total_revenue'].values[0] ])

    df_check = df4[1][df4[1].code==i]
    tmp_list.extend([ df_check['net_profit_to_total_revenue'].values[0] ])

    # operating_expense_to_total_revenue 营业费用/营业总收入(%)
    df_check = df4[0][df4[0].code==i]
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['operating_expense_to_total_revenue'].values[0] ])

    df_check = df4[1][df4[1].code==i]
    tmp_list.extend([ df_check['operating_expense_to_total_revenue'].values[0] ])

    # ga_expense_to_total_revenue   管理费用/营业总收入(%)
    df_check = df4[0][df4[0].code==i]
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['ga_expense_to_total_revenue'].values[0] ])

    df_check = df4[1][df4[1].code==i]
    tmp_list.extend([ df_check['ga_expense_to_total_revenue'].values[0] ])

    # financing_expense_to_total_revenue    财务费用/营业总收入(%)
    df_check = df4[0][df4[0].code==i]
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['financing_expense_to_total_revenue'].values[0] ])

    df_check = df4[1][df4[1].code==i]
    tmp_list.extend([ df_check['financing_expense_to_total_revenue'].values[0] ])

    # roe
    df_check = df4[0][df4[0].code==i]
    if df4[0][df4[0].code==i].empty:
        tmp_list.extend([0])
    else:
        tmp_list.extend([ df_check['roe'].values[0] ])

    df_check = df4[1][df4[1].code==i]
    tmp_list.extend([ df_check['roe'].values[0] ])

    check_list.append(tmp_list)
    
columns = ['code', u'name', u'xm'] + ['%s' %(str(year_watch[i])) for i in range(5)]\
        + [u'ly_净利', u'lly_净利', u'ly_营费', u'lly_营费', u'ly_管费', u'lly_管费', u'ly_财费', u'lly_财费'] \
        + [u'ly_roe', u'lly_roe']
watch_df4 = pd.DataFrame(data=check_list, columns=columns)

watch_df4
