import pandas as pd
dict={"country":["Brazil","Russia","India","China","South Africa"],
      "capital":["Brazilia","Moscow","New Dehli","Beijing","Pretoria"],
      "area":[8.516,17.10,3.286,9.597,1.221],
      "population":[200.4,143.5,1252,1357,52.98]}

brics=pd.DataFrame(dict)
print(brics)

brics.index=["BR","RU","IN","CH","SA"]
print(brics)

cars = pd.read_csv('cars.csv')
print(cars)

# # Print out country column as Pandas Series
# print(cars['cars_per_cap'])

# # Print out country column as Pandas DataFrame
# print(cars[['cars_per_cap']])

# # Print out DataFrame with country and drives_right columns
# print(cars[['cars_per_cap', 'country']])

print(cars[0:4])
print(cars[2:4])

print("---iloc---")
print(cars.iloc[2])
print("--loc---")
print(cars.loc[2])

print("--handling missing values---")
import numpy as np
df=pd.DataFrame({'A':[1,2,np.nan],
                 'B':[5,np.nan,np.nan],
                 'C':[1,2,3]})
print(df)
print(df.dropna())

print(df.dropna(axis=1))
print(df.dropna(thresh=2))

print(df.fillna(value='FILL VALUES'))
print(df['A'].fillna(value=df["A"].mean()))


