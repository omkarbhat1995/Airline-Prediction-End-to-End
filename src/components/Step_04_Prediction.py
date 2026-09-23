import joblib
import pandas as pd

class Pred_clening:

    def generate_Date_Time(self,df):

        df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'],format='mixed')

        df['D_Day'] = df['Date_of_Journey'].dt.day
        df['D_Month'] = df['Date_of_Journey'].dt.month
        df['D_Year'] = df['Date_of_Journey'].dt.year

        df['D_Hour'] = df['Date_of_Journey'].dt.hour
        df['D_Minute'] = df['Date_of_Journey'].dt.minute


        df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'],format='mixed')
        df['A_Hour'] = df['Arrival_Time'].dt.hour
        df['A_Minute'] = df['Arrival_Time'].dt.minute

        df['A_Day'] = df['Arrival_Time'].dt.day
        df['A_Month'] = df['Arrival_Time'].dt.month
        df['A_Year'] = df['Arrival_Time'].dt.year

        return df

    def duration(self,df):
        print("_______________Duration_____________")

        print(df)
        df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'],format='mixed')
        df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'],format='mixed')

        Time_Value = df['Arrival_Time'] - df['Date_of_Journey']
        print(Time_Value)
        Time_Value = Time_Value.dt.total_seconds() / 60
        df['DurHrs_Mins'] = Time_Value.astype(int)
        print(df.T)
        print("------Duration-S-Completed")
        return df

    def drop_Col_From_web(self,df):
        df = df.drop(['Date_of_Journey','Arrival_Time'],axis=1)
        return df

    def total_Stops(self, df):
        stop_mapping = {
                    "non-stop": 0,
                    "1 stop": 1,
                    "2 stops": 2,
                    "3 stops": 3,
                    "4 stops": 4,}
        print("------Data TotalStops-------")

        print(df)
        df["Total_Stops"] = df["Total_Stops"].replace(stop_mapping)
        print("------TotalStops Cleaned-------")

        return df


    def transform_input(self,df):
        # Load fitted transformer
        transform_file = joblib.load("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\trans_files\\Transform.pkl")
        # Transform input data
        df = transform_file.transform(df)

        return df
# Load model once
    def predict_output(self,df):
        MODEL_PATH = ("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\model_files\\Random_Forest_Reg.pkl")
        ml_model = joblib.load(MODEL_PATH)
        output = ml_model.predict(df)
        return output