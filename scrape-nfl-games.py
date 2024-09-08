from time import gmtime, strftime
import pandas as pd
import requests

from time import gmtime, strftime
import pandas as pd
import requests

def nfl_game_odds():
    #basically the only two things I had to change from the baseball scrip were the "sportid" (when defining API parameters at line 16) and reseting the index in the last command (line 27) so the DFs would both have the same number of columns
    """
    Fetches NFL game odds data from an external API and processes it into a structured pandas DataFrame.

    The function sends a GET request to the API endpoint with specific parameters to retrieve data 
    related to NFL games. It then extracts relevant information from the response JSON and organizes it 
    into a pandas DataFrame with game details, market details, and odds data.

    Returns:
        pd.DataFrame: A DataFrame containing information about NFL games, including game ID, 
                        game name, date, live status, URL, market count, and odds details.
    """
    # API endpoint and parameters for fetching NFL game data
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
        'sportIds': '14'
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from API. Status code: {response.status_code}")

    df = pd.DataFrame(response.json())
    new_df = df['markets'].apply(pd.Series).reset_index().melt(id_vars='index', var_name='key')
    new_df = pd.concat([new_df.drop('value', axis=1), new_df['value'].apply(pd.Series)], axis=1)
    new_df =new_df.reset_index()
    new_df2 = new_df['selections'].apply(pd.Series).reset_index().melt(id_vars='index', var_name='key')
    new_df2 = pd.concat([new_df2.drop('value', axis=1), new_df2['value'].apply(pd.Series)], axis=1)
    games=df.reset_index().merge(new_df,on="index").merge(new_df2,on="index").loc[:,['id_x', 'name_x', 'date', 'isLive_x', 'relativeDesktopUrl', 'openMarketCount', 'id_y', 'name_y', 'name', 'lx', 'odds', 'line', 'betTrend']]

    return games
  
games = nfl_game_odds()
games.to_csv("data/2024/nfl/nfl_games_"+strftime("%Y%m%d%H%M", gmtime())+".csv",index=False)
