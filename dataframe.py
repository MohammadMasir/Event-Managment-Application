import pandas as pd 
import matplotlib.pyplot as plt
data = {'name':['lucky','hansraj','gautam','rohit'],'age':[24,34,45,56]}
df = pd.DataFrame(data)
print(df)
df.plot(kind = 'hist', x = 'name', y = 'age', color = 'blue')
plt.title('histogram')
plt.show()