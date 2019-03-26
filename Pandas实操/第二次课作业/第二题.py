import pandas as pd

data = pd.read_excel('loans.xlsx')
# data.drop('每月归还额',axis=1,inplace=True)
del data['每月归还额']
# print(data.head(3))
# vc = data['贷款期限'].value_counts()   # 频数统计
# print(vc)
# group = data.groupby(data['还款状态'])['贷款金额'].mean()
# group = data['贷款金额'].groupby(data['还款状态']).mean()
# print(group)
# des = data['贷款金额'].describe().T
# des = data['贷款金额'].sum()
# print(des)
# data.sort_values(by=['发放贷款日期','贷款金额'],ascending=[False,True],inplace=True)
# print(data)
# data['每月归还额'] = (data['贷款金额']/data['贷款期限']).astype(int)
# print(data.head())
# da = data[data['账户号']>2000][data['账户号']<5000][['发放贷款日期','贷款金额']]
# print(da)