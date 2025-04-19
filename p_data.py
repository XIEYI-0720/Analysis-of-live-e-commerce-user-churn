import pandas as pd

# 读取数据
df = pd.read_excel('./Project Dataset.xlsx', engine='openpyxl', sheet_name='E Comm')

new_col=['客户ID','流失','任期','登录设备','城市等级','仓库到顾客地址平均距离', '婚姻状况','年龄组','性别','使用APP时间','上月订单数量','与去年相比的订单金额增长','距离上次订单的天数','上月首选订单类别','关注的直播者数量','满意度评分',
'上月投诉数','上月优惠券使用次数','上月折扣金额']
df.columns = new_col


# 查看数据基本信息 
print("数据基本信息：")
# print(df.info())
# for col in df.columns: 
#     print(f"{col}的唯一值：{df[col].unique()}")
#     print(f"{col}的类型：{df[col].dtype}")
#     print(f"{col}的缺失值数量：{df[col].isnull().sum()}")
#     print(f"{col}的缺失值比例：{df[col].isnull().sum()/len(df)}")
#     print(f"{col}的描述性统计：\n{df[col].describe()}\n")
# # 填充或删除缺失值 1
 

df['任期'] = df['任期'].fillna(df['任期'].mean()).astype('int')
cols_to_fill = ['仓库到顾客地址平均距离', '使用APP时间', 
               '与去年相比的订单金额增长', '距离上次订单的天数',
               '上月优惠券使用次数']
for col in cols_to_fill:  # 直接遍历目标列
    df[col] = df[col].fillna(df[col].median()).astype('int')
df['上月订单数量'] = df['上月订单数量'].replace(r'^\s*$', 0, regex=True).astype('float').fillna(0).astype('int')


# df.replace({'null': ''}, regex=True, inplace=True)
print("\n缺失值统计：",df.isnull().sum())


# # 检查重复值
# print("\n重复值统计：")
# print(df.duplicated().sum())
# 删除重复值
# df.drop_duplicates(inplace=True)


# 保存预处理后的数据
df.to_excel('./preprocessed_data.xlsx', index=False, engine='openpyxl', sheet_name='E Comm')

