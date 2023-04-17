from time import gmtime, strftime
import pandas as pd
import requests

def game_runs(game_id):
    try:
        url = 'https://offer.cdn.begmedia.com/api/pub/v5/events/'+game_id+'?application=1024&countrycode=pt&language=pt&sitecode=ptpt'
        response2 = requests.get(url)
        df3 = pd.DataFrame(response2.json()['grouped_markets'][1])
    except IndexError:
        # Handle the error here
        print("Erro")
        return
    df3 = df3.reset_index()
    dfaux2=df3['markets'].apply(pd.Series)
    dfaux3=dfaux2['selections'].apply(pd.Series)
    dfaux3.head()
    dfaux3.columns
    result_df = pd.DataFrame()
    #dfaux3[col].iloc[0,].apply(pd.Series).iloc[0,].apply(pd.Series)
    for col in dfaux3.columns:
        print(col)
        print(dfaux3[col].apply(pd.Series).iloc[0,].apply(pd.Series))
        res=dfaux3[col].apply(pd.Series).iloc[0,].apply(pd.Series)
        result_df= result_df.append(res, ignore_index=True)

    result_df = result_df.loc[:,['name','odds','is_cashoutable']]
    result_df.insert(loc=0, column='gameid',value=response2.json()['id'])
    result_df.insert(loc=1, column='date',value=response2.json()['date'])
    result_df.insert(loc=2, column='home',value=response2.json()['contestants'][0]['name'])
    result_df.insert(loc=3, column='away',value=response2.json()['contestants'][1]['name'])
    result_df.insert(loc=4, column='competition',value=response2.json()['competition']['name'])
    return result_df

def game_odds():
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
    return games

games = game_odds()

result_dfs = []
game_ids=pd.DataFrame({'id': games['id_x'].unique()})
game_ids['id']=game_ids['id'].astype(str)
# Loop over each ID in the DataFrame and call the function
for id in game_ids['id']:
    result_dfs.append(game_runs(id))

# Concatenate the resulting DataFrames into a single DataFrame
run_odds = pd.concat(result_dfs, ignore_index=True)

run_odds.to_csv("data/baseballrunodds"+strftime("%Y%m%d%H%M", gmtime())+".csv",index=False)
games.to_csv("data/baseballgames"+strftime("%Y%m%d%H%M", gmtime())+".csv",index=False)
