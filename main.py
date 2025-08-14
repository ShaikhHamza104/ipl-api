import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Import dataset
try:
    df = pd.read_csv('ipl_clean.csv',low_memory=False)
except FileNotFoundError:
    raise Exception("ipl_clean.csv file not found.")
df['season'] = df['season'].str.split('/').str[0]
@app.get('/')
def root():
    return {
        "Message": "Success",
        "Mode": "Online",
        "Created By": "Hamza",
    }

@app.get('/api/matches/id/{match_id}')
def get_match_by_id(match_id: int):
    match = df[df['id'] == match_id]
    if match.empty:
        return {"error": "Match not found"}
    return match.to_dict(orient='records')

@app.get('/api/matches/{year}')
def season(year: str, limit: int = 5):
    year_df = df[df['season'] == year]
    response = {
        f"{year} Year": year_df.head(limit).to_dict(orient='records'),
        "shape": {
            "rows": year_df.shape[0],
            "columns": year_df.shape[1]
        }
    }
    return response


@app.get('/api/allteams')
def teams():
    teams = pd.unique(df['team1'].values.tolist()+df['team2'].values.tolist())
    response = {
        "Teams": teams.tolist()
    }
    return response
@app.get('/api/matches/venue/{venue_name}')
def venu(venue_name: str):
    venue_df = df[df['venue'].str.lower() == venue_name.lower()]
    
    result = (
        venue_df.groupby(['team1', 'team2'])
        .size()
        .sort_values(ascending=False)
        .reset_index(name='match_count')
        .to_dict(orient='records')  # List of dicts, JSON-friendly
    )
    
    return result
