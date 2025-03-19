language_percentage = {'JavaScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, 'TypeScript': 38.5} #create the dictionary
print(language_percentage)

import matplotlib.pyplot as plt
languages = list(language_percentage.keys()) #create the x label
percentages = list(language_percentage.values()) #create the y label
plt.bar(languages, percentages, color="pink") #create the bar
plt.xlabel('Programming Languages') #name the x label
plt.ylabel('Percentage of Developers') #name the y label
plt.title('Top 5 Programming Language Popularity') #name the bar
plt.ylim(0, 70) #limit the y value from 0 to 70
plt.show() #show the bar

requested_language = 'Python'  #a variable of the requested	activity that can be modified
percentage = language_percentage.get(requested_language)
if percentage is not None:
    print(f"\nThe percentage of developers who use {requested_language} is {percentage}%.")
else:
    print(f"\n{requested_language} is not in the top 5 languages.")
