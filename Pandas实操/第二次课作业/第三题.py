import pandas as pd
data = pd.read_excel('product_orders.xlsx')
print(data.info())
# 数据透视表
pt = pd.pivot_table(data,'Customer_Country',
               'Customer_Age_Group','Customer_Gender','count')
print(pt)
# pt['Female Percent'] = (pt['F']/(pt['F']+pt['M'])).map(lambda x:format(x,'.0%'))
# pt['Male Percent'] = (pt['M']/(pt['F']+pt['M'])).map(lambda x:format(x,'.0%'))
# print(pt)

print('------------打印列百分比------------')
print(pt.apply(lambda x:x/x.sum(),axis=0))
print('------------打印行百分比-------------')
print(pt.apply(lambda x:x/x.sum(),axis=1))