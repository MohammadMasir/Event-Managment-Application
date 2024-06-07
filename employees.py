import pandas as pd
import matplotlib.pyplot as plt
data={'name':['lucky','hansraj','dhruv','narayan','ghevar','dilip','sahil','jagruti','siddharth','aniket'],'company_name':['TCS','INFOSYS','HCL','HINDUSTHAN UNILIVER','CEAT','MRF','KOKABURA','BAS','NEW BALANCE','ENGLISH WILLOW'],'salary':[10000,20000,30000,40000,500000,600000,700000,800000,90000,100000]}
df=pd.DataFrame(data)
print(df)
df.plot(kind='bar',x='name',y='salary',color='yellow')
plt.title('scatterplot')
plt.show()

