import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

class PlayerSimilarity:
    def __init__(self, df):
        self.df = pd.DataFrame(df)
        self.scaler = StandardScaler()
        self.model = NearestNeighbors(n_neighbors=6)
        
    def Player_finder(self, Player_name):
        self.all_features = ['Batting_avg', 'Batting_strikerate',
                             'Batting_total_runs', 'Batting_boundary', 'Batting_dot',
                             'Bowling_balls', 'Bowling_over', 'Bowling_runs', 'Bowling_economy',
                             'Bowling_wickets', 'Bowling_total_runs', 'Bowling_avg',
                             'Bowling_strikerate']
        
        # Standardize all features
        self.df[self.all_features] = self.scaler.fit_transform(self.df[self.all_features])
        
        # Fit and find similar players
        self.model.fit(self.df[self.all_features])
        self.query_player = self.df[self.df['Player_name'] == Player_name][self.all_features]
        self.distances, self.indices = self.model.kneighbors(self.query_player)
        self.similar_players = self.df.iloc[self.indices[0]]['Player_name'].values
        return self.similar_players[1:]
        
    def Bowler_finder(self, Player_name):
        self.bowler_features = ['Bowling_balls', 'Bowling_over', 'Bowling_runs', 'Bowling_economy',
                                'Bowling_wickets', 'Bowling_total_runs', 'Bowling_avg', 'Bowling_strikerate']
        
        # Standardize bowler features
        self.df[self.bowler_features] = self.scaler.fit_transform(self.df[self.bowler_features])
        
        # Fit and find similar bowlers
        self.model.fit(self.df[self.bowler_features])
        self.query_player = self.df[self.df['Player_name'] == Player_name][self.bowler_features]
        self.distances, self.indices = self.model.kneighbors(self.query_player)
        self.similar_players = self.df.iloc[self.indices[0]]['Player_name'].values
        return self.similar_players[1:]
        
    def Batsmen_finder(self, Player_name):
        self.batter_features = ['Batting_avg', 'Batting_strikerate',
                                'Batting_total_runs', 'Batting_boundary', 'Batting_dot']
        
        # Standardize batter features
        self.df[self.batter_features] = self.scaler.fit_transform(self.df[self.batter_features])
        
        # Fit and find similar batsmen
        self.model.fit(self.df[self.batter_features])
        self.query_player = self.df[self.df['Player_name'] == Player_name][self.batter_features]
        self.distances, self.indices = self.model.kneighbors(self.query_player)
        self.similar_players = self.df.iloc[self.indices[0]]['Player_name'].values
        return self.similar_players[1:]
