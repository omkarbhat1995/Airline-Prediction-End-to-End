import pandas as pd
from sklearn.model_selection import train_test_split

class Cleaning:
    def __init__(self):
        pass
    def read_data(self,filepath):
        df = pd.read_csv(filepath)
        return df
    def data_cleaning(self,df):
        pass
    def total_stops(self,df):
        pass
    def process_duration(self,df):
        pass
