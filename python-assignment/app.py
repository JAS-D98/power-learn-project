# ++++++++++++++ Using Numpy for arithmetic ++++++++++++++++++++
# import numpy as np

# array=np.array([30, 10, 56, 31, 23])
# max_value=np.max(array)
# min_value=np.min(array)

# print("Max Value", max_value)
# print("Min_Value", min_value)


# ++++++++++++++ Using pandas to handle files ++++++++++++++++++++
# import pandas as pd

# Names={
#     'Name':['James', 'Phillip', 'Halima'],
#     'Age':[20, 16, 18],
#     'Grade':[70, 16, 30]
# }

# dataFrame=pd.DataFrame(Names)

# print(dataFrame)

# print(dataFrame[dataFrame['Grade']>50])

# ++++++++++++++ Using matplotlib to handle graphs and charts ++++++++++++++++++++
# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# # Create a line plot
# plt.plot(x, y)
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# import requests
# response=requests.get("https://restcountries.com/v3.1/all")
# print (response.json())

import pandas as pd
import matplotlib.pyplot as plt

data={
    'Country':['China','India', 'United','Indonesia','Nigeria'],
    'Population':[1411778724 ,1407563842 ,331893745 ,273523615 ,206139589]
}

dataFrame=pd.DataFrame(data)
print(dataFrame)

# pie chart
plt.plot(dataFrame['Country'], dataFrame['Population'])
plt.title('Country Census')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()


# bar graph
countries=['China','India', 'United','Indonesia','Nigeria']
population=[1411778724 ,1407563842 ,331893745 ,273523615 ,206139589]

plt.bar(countries, population, color="red")
plt.title('Bar Census')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.show()

# Pie graph
countries=['China','India', 'United','Indonesia','Nigeria']
population=[1411778724 ,1407563842 ,331893745 ,273523615 ,206139589]

plt.pie(population, labels=countries, autopct='%1.1f%%')
plt.title('Pie Census')
plt.show()

# histogram
ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()