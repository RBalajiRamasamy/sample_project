import pandas as pd

x = ["apple", "banana", "cherry"]
# for i in x:
#     #print(i)
#     if i=='apple':
#         print('true')
#         x.append('append')
#     else:
#         print("false")
# Convert to DataFrame
df = pd.DataFrame(x, columns=['Name'])
#print(df)
#df.to_excel('df.xlsx',sheet_name='Data',index=False)
# writer = pd.ExcelWriter("dataframe.xlsx", engine='xlsxwriter')
# df.to_excel(writer,sheet_name = 'dataframe', index=False)

