import pandas as pd
df=pd.read_excel("demo.xlsx",sheet_name="Sheet1",usecols=['Name'],nrows=2)
print(df)


# read_excel -->used for excel
# sheet_name-->specify ths sheet name u want to read 
# usecols -->specify the column name you want to read
# nrows -->rows  u want to read