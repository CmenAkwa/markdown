# PassengerId Survived:0死1活 Pclass:船舱等级 Name Sex Age SibSp兄弟姐妹和配偶数量 Parch父母子女数量 Ticket票号 Fare票价 Cabin座位号 Embarked登船码头
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

plt.rc("font", family='YouYuan')  # 中文乱码解决
warnings.filterwarnings('ignore')
df = pd.read_csv('train.csv', encoding='utf-8', header=0, index_col=0)
# 年龄缺失,座位号缺失,码头缺失
'''judge = df.duplicated(keep=False)
for i in judge:
    if i == True:
        print('have')'''  # 检测发现数据集没有重复行
# print(df["Sex"].unique())
# print(df["Age"].unique())
'''df["Age"].fillna(df["Age"].median(), inplace=True)  # 将年龄缺失值替换成中位数'''  # 造成数据不准,不使用
# print(df["Age"].unique())
# print(df.describe())
# 总体生还率
n = df['Survived'].value_counts()  # n为一个series
plt.figure(figsize=(5, 5))
plt.pie(n, autopct='%0.1f%%', labels=['死亡', '存活'], pctdistance=0.5, labeldistance=1.1,
        shadow=True, explode=[0, 0.1], textprops=dict(size=20))
plt.title("存活率饼图")
plt.show()
# 性别下的生还率
sex_count = df.groupby(by='Sex')['Survived'].value_counts()
axes1 = plt.subplot(1, 2, 1)  # 1行2列1号
axes1.pie(sex_count.loc['female'], autopct='%.1f%%', labels=['存活', '死亡'], pctdistance=0.5, labeldistance=1.1,
          shadow=True, explode=[0, 0.2], textprops=dict(size=15), colors=['#EADDF2', '#8775D3'])
axes1.set_title('女性生还率')
axes2 = plt.subplot(1, 2, 2)
axes2.pie(sex_count.loc['male'], autopct='%.1f%%', labels=['死亡', '存活'], pctdistance=0.5, labeldistance=1.1,
          shadow=True, explode=[0, 0.2], textprops=dict(size=15), colors=['#8775D3', '#EADDF2'])
axes2.set_title('男性生还率')
plt.show()

age_range = df['Age']
print(age_range.min(), age_range.max())
# 各年龄阶段人数
bins1 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
age_groups = pd.cut(df['Age'], bins=bins1)
age_counts = age_groups.value_counts()
count_array = age_counts.sort_index().values
print(count_array)

# 各年龄阶段生还人数
# print(age_num)
age_survived = []
for age in range(5, 81, 5):
    survived_num = df.loc[(age_range >= age - 5) & (age_range <= age)]['Survived'].sum()
    age_survived.append(survived_num)
print(age_survived)
# 绘制条形图
plt.figure(figsize=(12, 6))
plt.bar(np.arange(2, 78, 5)+0.5,count_array, width=5, label='总人数', alpha=0.8)
plt.bar(np.arange(2, 78, 5)+0.5, age_survived, width=5, label='生还人数')
plt.xticks(range(0, 81, 5))
plt.yticks(range(0, 121, 10))
plt.xlabel('年龄', position=(0.95, 0), fontsize=15)
plt.ylabel('人数', position=(0, 0.95), fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(True,linestyle='--',alpha=0.6)
plt.show()

