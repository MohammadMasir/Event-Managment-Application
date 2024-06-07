import pandas as pd
data = {'empname':['lucky','manisha','tanvi','narayan'],'empno':[45,56,89,34],'designation':['developer','developer','doctor','civil engineer'],'salary':[5000,45000,56000,3000]}
df = pd.DataFrame(data)
print(df)
if 'salary'>10000:
    print(data)


