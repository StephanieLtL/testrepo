import pandas as pd            #导入pandas模块
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('data.xlsx')  #读取Excel文件
print(df.head())               #显示前5条数据

### My jupyter notebook code ###
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel(r'C:\Users\Stephanie\OneDrive\Documents\Python Scripts\Code\03\01\data.xlsx')
print(df.head())