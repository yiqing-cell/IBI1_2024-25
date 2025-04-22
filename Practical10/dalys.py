import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Lucas/Desktop/8001/ICBM/Week1/IBI1_2024-25/Practical10") 
  
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.iloc[0:10,2]) #1999  was the 10th year with DALYs data recorded in Afghanistan

is_1990 = dalys_data["Year"] == 1990
dalys_1990 = dalys_data.loc[is_1990, "DALYs"]
print("\n1990年所有国家的DALYs:")
print(dalys_1990)

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == 'France', ['DALYs', 'Year']]
mean_uk_dalys = uk['DALYs'].mean()
mean_france_dalys = france['DALYs'].mean()
print(f"Mean DALYs in UK: {mean_uk_dalys}")
print(f"Mean DALYs in France: {mean_france_dalys}") # the mean DALYs in the UK was greater than France
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in the UK Over Time')
plt.show()

china = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
plt.figure(figsize=(10, 6))
plt.plot(uk.Year, uk.DALYs, "bo", label="United Kingdom")
plt.plot(china.Year, china.DALYs, "r+", label="China")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs Comparison: UK vs China")
plt.xticks(rotation=45)
plt.legend()
plt.show()