# Estimating Long-Term Runoff using Regional Regression

Water Survey of Canada is the government organization that maintains a nation-wide network of streamflow monitoring stations.  There are roughly 2100 active monitoring stations in Canada, and while this is a large number, it is small in comparison to the number of streams and rivers, and the distribution of stations is biased to developed areas.

![Active Hydrometric Monitoring Stations in Canada](img/CAN_network_map.png)
>Realtime flow monitoring (source: Hamilton, Stuart. (0002). Winter Hydrometry: Real-Time Data Issues.

In addition to the active stations, there are roughly 6000 inactive stations where historical data can be drawn from.  This data is free, and openly available to the public through [Environment Canada's Datamart web portal](https://wateroffice.ec.gc.ca/mainmenu/real_time_data_index_e.html).

Open the datamart in a new window and go to the **Map Search**.  Choose BC as the "Province or Territory" and click on **"Go"**.  A map view of hydrometric stations in BC will render in your browser.  

Zoom into the region east of Vancouver, in the region of Harrison Lake, as shown below.  There are two stars drawn (excellently) on the map indicating locations we're interested in for run-of-river hydro.  

In order to figure out how much water we might expect in the basins where the stars are drawn, we need to look at long-term measured records in the nearby area.  

![Map of active stations near Harrison Lake](img/harrison_lake_map1.png)
>Map of active stations near Harrison Lake (source: Water Survey of Canada)

Using the map view, retrieve the station ID numbers and store them as **strings** in different variables.  i.e.:

`stn1 = '08EA004'`  <-- here the single quote `'` surrounding a group of characters makes a string.

# find the three station numbers and store them in three variables
stn1 = '' 
stn2 = ''
stn3 = ''

Below we are going to access daily flows for these stations directly from Datamart.

**Note**: Datamart is for realtime and recent data.  You can find long-ter records for these stations using the [BC Water Tool](https://kwt.bcwatertool.ca/streamflow).

# you can get daily data for the last month
datamart_link_daily = 'https://dd.weather.gc.ca/hydrometric/csv/BC/daily/'
# you can also get hourly data for the latest 24 hours
datamart_link_daily = 'https://dd.weather.gc.ca/hydrometric/csv/BC/daily/'

# pandas is a library for manipulating large amounts of data,
# sort of like Excel without a user interface.
import pandas as pd

stn1 = '08MG001'
filename = f'BC_{stn1}_daily_hydrometric.csv'

# import the data for the first station
df1 = pd.read_csv(datamart_link + filename, 
                  parse_dates=['Date'], index_col='Date',
                 infer_datetime_format=True)
# the 'head' command shows a preview of the data we've downloaded
df1.head()

We want to compare flow at the three stations.  Let's put all of the data together into one dataframe.

# create an empty list
all_dfs = []

stn1, stn2, stn3 = '08MH147', '08MF065', '08MG001'
# create a list of the station names
station_list = [stn1, stn2, stn3]

# loop through the filenames and store each dataframe in the list

for station in station_list:
    print(f'Downloading data for {station}...')
    filename = f'BC_{station}_daily_hydrometric.csv'
    df = pd.read_csv(datamart_link + filename, 
                  parse_dates=['Date'], index_col='Date',
                 infer_datetime_format=True)
    
    # create a short form name so we can easily index the column
    # using the station number
    df[station] = df['Discharge / Débit (cms)']
    
    # append the dataframe to the list 
    all_dfs.append(df)

# concatenate the list of dataframes into a single dataframe
# inner join means to keep only concurrent data (flow values on the same day)
data = pd.concat(all_dfs, join='inner', axis=1)
# keep just the flow columns
data = data[[stn1, stn2, stn3]]
data.head()

data.plot()

Now let's compare the three using linear regression.

[Background information on Linear Regression](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/introduction-to-trend-lines/a/linear-regression-review).

from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# this makes the figure render within jupyter instead of a new window
output_notebook()

p = figure(width=600, height=400, title=f'{stn1} vs. {stn2}')

p.circle(data[stn1], data[stn2])
show(p)

p = figure(width=600, height=400, title=f'{stn1} vs. {stn2}')

p.circle(data[stn1], data[stn3])
show(p)

p = figure(width=600, height=400, title=f'{stn1} vs. {stn2}')

p.circle(data[stn2], data[stn3])
show(p)

lt_dfs = []

for stn in station_list:
    # I saved long-term data ahead of time in the 'data/' folder
    filename = f'data/{stn}.csv'
    
    df = pd.read_csv(filename, header=13,
                  parse_dates=['Datetime'], index_col='Datetime',
                 infer_datetime_format=True)
    # how many analysis types are there?
    print(list(set(df['Analysis'])))
    
    # we want just the flow data, not stage!
    df = df[df['Analysis'] == 'Discharge (m3/s)']
    
    # 'Value' isn't really helpful, create a column using our station number
    df[stn] = df['Value']
    
    print(df.head())
    lt_dfs.append(df)

lt_df = pd.concat(lt_dfs, join='inner', axis=1)[station_list]

lt_df.head()

num_days = len(lt_df)
print(f'There are {num_days} days of concurrent record between {station_list}')

lt_df.plot()

Find the long-term mean annual discharge (**MAD**) for these three sites.


lt_df.mean()

These mean annual flow numbers look pretty similar.  

>So can we just use this number for our basin and calculate energy?



### Unit-Area Runoff

**How do the three stations compare on a unit-area basis?**

Unit area runoff is commonly expressed in $\frac{L}{s \cdot km^2}$ or $mm$.

$$1 \frac{ \so{m^3} }{s} \cdot 1000 \frac{L}{m^3} \div A km^2 = UR \frac{L}{s\cdot km^2}$$

stn_das = {'08MF065': 712,
          '08MH147': 290,
          '08MG001': 383}

# make a copy of the flow dataframe
lt_ur = lt_df.copy()
for stn in station_list:
    lt_ur[stn] = 1000 * lt_ur[stn] / stn_das[stn]

lt_ur.head()

# re-calculate the mean on a unit-area basis
lt_ur.mean()

