import gmaps
import gmaps.datasets
# Use google maps api
gmaps.configure(api_key='AIzaSyBgHX9zR1sE5MBCTahBhlhvE7hhsjd1W30') # Fill in with your API key
# Get the dataset
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
#Get the locations from the data set
locations = earthquake_df[['latitude', 'longitude']]
#Get the magnitude from the data
weights = earthquake_df['magnitude']
#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
