from time import gmtime, strftime
import pandas as pd
import requests

url = 'https://offer.cdn.begmedia.com/api/pub/v4/events'
params = {
    'application': '1024',
    'countrycode': 'pt',
    'hasSwitchMtc': 'true',
    'language': 'pt',
    'limit': '50',
    'offset': '0',
    'sitecode': 'ptpt',
    'sortBy': 'ByLiveRankingPreliveDate',
    'sportIds': '20'
}

response = requests.get(url, params=params)
response
df = pd.DataFrame(response.json())
df = df.reset_index()
new_df = df['markets'].apply(pd.Series).reset_index().melt(id_vars='index', var_name='key')
new_df = pd.concat([new_df.drop('value', axis=1), new_df['value'].apply(pd.Series)], axis=1)
new_df =new_df.reset_index()
new_df2 = new_df['selections'].apply(pd.Series).reset_index().melt(id_vars='index', var_name='key')
new_df2 = pd.concat([new_df2.drop('value', axis=1), new_df2['value'].apply(pd.Series)], axis=1)
games=df.merge(new_df,on="index").merge(new_df2,on="index").loc[:,['id_x', 'name_x', 'date', 'isLive_x', 'relativeDesktopUrl', 'openMarketCount', 'id_y', 'name_y', 'name', 'lx', 'odds', 'line', 'betTrend']]
games.to_csv("data/baseballgames"+strftime("%Y%m%d%H%M", gmtime())+".csv",index=False)
