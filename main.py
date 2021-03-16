import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# import data
#df = pd.read_csv(r'C:\Users\wzc03\OneDrive\桌面\Spring 2021 MDI\2020_dem_vote_share.csv')
#plt.hist(df['candidate'],bins=50)
#plt.show()

plt.scatter(df['ad_spend'],df['votes'])
plt.show()

#fig = px.line(df,x='candidate', y='ad_spend', title="Vote vs. Ad Spend")
#fig.show()

# data = pd.read_csv(r'C:\Users\wzc03\OneDrive\桌面\Spring 2021 MDI\2020_dem_vote_share.csv')
#time = [0, 1, 2, 3]
#position = [0, 100, 200, 300]

#plt.plot(time, position)
#plt.xlabel('Time (hr)')
#plt.ylabel('Position (km)')
#plt.show()

# histogram
#plt.hist(df['candidate'], bins=50)
#plt.show()

# histogram of transformed scale
#df['log_pop'] = np.log(df['candidate'])
#plt.hist(df.log_pop,bins=50)
#plt.show()

"""
plt.scatter("votes","ad_spend")
plt.title("Graph")
plt.xlabel("Votes")
plt.ylabel("Ad Spend")

plt.show()

"""
#df.plot()
#df.plot(kind='scatter', x='votes', y='ad_spend')
