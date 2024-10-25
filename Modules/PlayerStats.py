class PlayerStats:
    def __init__(self,df):
        self.df = df
    def FetchOverallStats(self,playername):
        self.playername = playername
        return (self.df[self.df["Player_name"]==self.playername])
    def FetchBattingStats(self,playername):
        self.playername = playername
        return (self.df[self.df["Player_name"]==self.playername]).iloc[:,:5]
    def FetchBowlingStats(self,playername):
        self.playername = playername
        return (self.df[self.df["Player_name"]==self.playername]).iloc[:,[0,6,7,8,9,10,11,12,13]]