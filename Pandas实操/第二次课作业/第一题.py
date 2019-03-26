import pandas as pd

file1 = 'supplier_country_sales.xlsx'
# data1 = pd.read_excel(file1)
# data2 = data1.T
# data2.drop('Year',axis=0,inplace=True)
# data2.rename(columns={0:2003,1:2004,2:2005,3:2006,4:2007},inplace=True)
# print(data2)
data1 = pd.read_excel(file1, index_col='Year')
data2 = data1.T
# data2.to_excel('data2.xls')
data2.index.name = 'Country'
data2.columns.name = ''
print(data2)
