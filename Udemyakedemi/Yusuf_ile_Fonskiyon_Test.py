import numpy as np
import pandas as pd

df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\AKEDEMİK\Udemyakedemi\ToExcel.xlsx')
yusuf = df.fillna(31)
ysuuf = df.replace(np.nan,0)
print(ysuuf)
print(yusuf)

