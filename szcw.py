# 发展指标
# 主营业务收入（ operating_revenue ）增长率 
# 主营业务收入增长的含金量
# 净利润 net_profit 

import pandas as pd

watch_list = ['000001.XSHE']
all_stcok = get_all_securities(['stock'])

q = query(
    income.code, income.operating_revenue, income.net_profit
).filter(
    valuation.code.in_(watch_list)
)
df = get_fundamentals(q, statDate='2015')

check_list = []
y_danwei = 100000000
for i in watch_list:
    df_check = df[df.code==i]
    check_list.append([i, all_stcok.ix[i].display_name.replace(' ', ''),round(df_check['operating_revenue'].values[0]/y_danwei,3), \
    round(df_check['net_profit'].values[0]/y_danwei,3)])
    
columns=[u'code', u'名称', u'主收入（亿）', u'净利润（亿）']
df_watch= pd.DataFrame(data=check_list, columns=columns)
df_watch
