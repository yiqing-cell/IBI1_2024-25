# UK data: country names and populations
uk_data = {'England': 57.11, 'Wales': 3.13, 'Northern Ireland': 1.91, 'Scotland': 5.45}
# China data: provinces bordering Zhejiang and populations
china_data = {'Fujian': 41.88, 'Jiangxi': 45.28, 'Anhui': 61.27, 'Jiangsu': 85.15}
# Sort UK populations
sorted_uk = sorted(uk_data.values())
print("Sorted UK populations (millions):", sorted_uk)
# Sort China populations
sorted_china = sorted(china_data.values())
print("Sorted Zhejiang-neighbouring provinces populations (millions):", sorted_china)

import matplotlib.pyplot as plt
# UK Pie Chart
labels1 = list(uk_data.keys())  # Convert keys to a list
sizes1 = list(uk_data.values())  # Use original values for pie chart
plt.figure(figsize=(8, 4))  # Create a new figure
plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90) #create the uk pie chart
plt.title('UK Population Distribution', fontsize=14, pad=20) #name the uk pie chart
plt.axis('equal')  # Ensure the pie is circular

# China Pie Chart
labels2 = list(china_data.keys())  # Convert keys to a list
sizes2 = list(china_data.values())  # Use original values for pie chart 
plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90) #create the chins pie chart
plt.title('Chinese Provinces Bordering Zhejiang', fontsize=14, pad=20) #name the china pie chart
plt.axis('equal')  # Ensure the pie is circular

plt.show()