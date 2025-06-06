# line
df2.plot(x='Year', y='Unemployment_Rate', kind='line', color='red')

# bar
df3.plot(x='Country', y='GDP_Per_Capita', kind='bar', title='GDP per capita per country')

# pie
df4.plot(y='Tasks', kind='pie', startangle=90)