#todo 多行业分析

hy_list =['C22', 'C29']
watch_list233 = [get_industry_stocks(i) for i in hy_list]
#'C22'
#'C29'
q233 = [query(
    income.code, income.operating_revenue, balance.account_receivable,
    income.operating_cost, balance.inventories, balance.fixed_assets,
    balance.total_sheet_owner_equities
).filter(
    valuation.code.in_(watch_list233[0]))  for i in range(len(hy_list))]

df3233 = [[get_fundamentals(q233[j], statDate=year_watch[i]) for i in range(3) ] for j in range(len(hy_list))]