import joblib

class Pred_clening:
    def duration(self, df):
        Time_Value = df['Arrival_Time'] - df['Date_of_Journey']
        print(Time_Value)
        Time_Value = Time_Value.dt.total_seconds() / 60
        df['DurHrs_Mins'] = Time_Value.astype(int)
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
        print("------Data TotalStops-------")

        return df


    def transform_input(self,df):
        # Load fitted transformer
        transform_file = joblib.load("E:/1.Eathans/Final Projects/Airline_ML_02_pra/Artifact/transFile/Transform.pkl")
        # Transform input data
        df = transform_file.transform(df)

        return df
# Load model once
    def predict_output(self,df):
        MODEL_PATH = ("E:/1.Eathans/Final Projects/Airline_ML_02_pra/Artifact/Model_File/Random_Forest_Reg.pkl")
        ml_model = joblib.load(MODEL_PATH)
        output = ml_model.predict(df)
        return output