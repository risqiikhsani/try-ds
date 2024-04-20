import pandas as pd

health_data = pd.read_csv("data2.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)

# remove blank arrows
health_data.dropna(axis=0,inplace=True)

print(health_data) 

# data type check
print(health_data.info())

# clean data if type not match
# health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
# health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

# print (health_data.info()) 

# analyze data
print(health_data.describe())
