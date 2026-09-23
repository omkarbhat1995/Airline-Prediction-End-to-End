import pandas as pd
import sys
import joblib
from src.components.Step_04_Prediction import Pred_clening

class CustomData:
    def __init__(self):
        self.PredObj = Pred_clening()

    def receiveDataFromWeb(self,Airline:str,Date_of_Journey:str,Source:str,
                               Destination:str,Arrival_Time:str,
                               Total_Stops:str):
        inputDict = {
                "Airline": [Airline],
                "Date_of_Journey": [Date_of_Journey],
                "Source": [Source],
                "Destination": [Destination],
                "Arrival_Time": [Arrival_Time],
                "DurHrs_Mins": [0],
                "Total_Stops": [Total_Stops]

            }
        df =  pd.DataFrame(inputDict)

        df = self.PredObj.total_Stops(df)
        df = self.PredObj.duration(df)
        df = self.PredObj.generate_Date_Time(df)
        df = self.PredObj.drop_Col_From_web(df)
        df = self.PredObj.transform_input(df)
        output = self.PredObj.predict_output(df)
        print(output)
        return output

    def clean_Data(self,df):
        print(df)
        df = self.PredObj.duration(df)



        return df