'''
line 1
'''
!pip install mlxtend --user
'''
line 2
'''
import pandas as pd
data = pd.read_csv('order.csv', encoding = 'gbk')
data
'''
line 3
'''
data['产品名称'] = data['产品名称'].apply(lambda x: x + ',')
transactions = data.groupby(['客户ID'])['产品名称'].sum().to_list()
transactions
'''
line 4
'''
data = pd.DataFrame(transactions)
data_ = data.drop(data.columns[0],axis=1).join(data[0].str.get_dummies(sep=','))
data_
'''
line 5
'''
from mlxtend.frequent_patterns import apriori as ap
from mlxtend.frequent_patterns import association_rules
# 求频繁项集
frequent_itemsets = ap(data_,min_support=0.05,use_colnames=True)
frequent_itemsets
'''
line 6
'''
# 求关联规则：
association_rule = association_rules(frequent_itemsets,metric='lift',min_threshold=1.1)
association_rule.sort_values(by='lift',ascending=False,inplace=True)
association_rule.reset_index(drop=True)