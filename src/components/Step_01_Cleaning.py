import pandas as pd
from sklearn.model_selection import train_test_split 


class cleaning:
    def __init__(self):
        pass
    def readData(self):
        filePath ="G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//Airline1.csv"
        df = pd.read_csv(filePath)
        return df

    def DataCleaning(self,df):
        Missing_Total_Stops = df['Total_Stops'].mode()[0]
        Missing_Source = df['Source'].mode()[0]
        Missing_Destination = df['Destination'].mode()[0]
        Missing_Route = df['Route'].mode()[0]
        Missing_Price = df['Price'].mean()

        df.fillna(
                    {
                        'Total_Stops': Missing_Total_Stops,
                        'Source': Missing_Source,
                        'Destination': Missing_Destination,
                        'Route': Missing_Route,
                        'Price': Missing_Price,
                    },
                    inplace=True,
                )
        df['Destination'] = df['Destination'].replace({"New Delhi":"Delhi"})
        df['Total_Stops'] = df['Total_Stops'].replace({'non-stop':0, '2 stops':2, '1 stop':1, '3 stops':3,'4 stops':4})
        return df




    def process_duration(self,df):
        # df["DurHrs_Mins"] = 0
        for i in df.index:
            DurCol = df.loc[i, "Duration"]
            if " " in DurCol:
                colOne = DurCol.split(" ")[0]
                colTwo = DurCol.split(" ")[1]

                if "h" in colOne:
                    colOne = int(colOne.replace("h", "")) * 60
                elif "m" in colOne:
                    colOne = int(colOne.replace("m", ""))

                if "h" in colTwo:
                    colTwo = int(colTwo.replace("h", "")) * 60
                elif "m" in colTwo:
                    colTwo = int(colTwo.replace("m", ""))
                df.loc[i, "DurHrs_Mins"] = colOne + colTwo

            else:
                if "h" in DurCol:
                    DurCol = int(DurCol.replace("h", "")) * 60
                    df.loc[i, "DurHrs_Mins"] = DurCol
                elif "m" in DurCol:
                    DurCol = int(DurCol.replace("m", ""))
                    df.loc[i, "DurHrs_Mins"] = DurCol
        print("----clns-----")
        return df

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

    def drop_unesseary_Col(self,df):
        df = df.drop(['ID','Additional_Info','Route','Date_of_Journey','Dep_Time','Arrival_Time','Duration'],axis=1)
        return df

   
    def remove_Outlier(self,df):
        df['Airline'].unique()
        airlineName = { 'IndiGo':      [0.25,0.75],
                        "Air India":   [0.27,0.75],
                        'Jet Airways': [0.27,0.75],
                        'SpiceJet':    [0.10,0.60],
                        'Multiple carriers':[0.20,0.80],
                        'GoAir':       [0.20,0.75],
                        'Vistara':     [0.20,0.75],
                        'Air Asia':    [0.25,0.75],
                        'Vistara Premium economy':[0.25,0.75],
                        'Jet Airways Business':[0.25,0.75],
                        'Multiple carriers Premium economy':[0.20,0.75],
                        'Trujet':       [0,0]

                    }


        final_df = pd.DataFrame(columns=list(df.columns))
        for key,value in airlineName.items():
            airDataSet = ""
            airDataSet = df[df['Airline'] == key]

            q1 = airDataSet['Price'].quantile(value[0])
            q3 = airDataSet['Price'].quantile(value[1])
            IQR = q3-q1
            lowerLimit = q1-IQR*1.5
            upperLimit = q3+IQR*1.5
            lowerLimitIndex = airDataSet[airDataSet['Price']<=lowerLimit].index
            upperLimitIndex = airDataSet[airDataSet['Price']>=upperLimit].index

            if airDataSet.shape[0] > 5 : 
                airDataSet.drop(lowerLimitIndex,axis=0,inplace=True)
                airDataSet.drop(upperLimitIndex,axis=0,inplace=True)
            else:
                pass

            df[df.index.isin([2878])]
            #airDataSet1 = airDataSet1.append(airDataSet, ignore_index=True)  # ignore_index=True resets the index
            final_df = pd.concat([final_df, airDataSet], axis=0)  # axis=0 is the default and means appending vertically
            df = final_df
            return df

    def split_X_y(self,df):
        y = df['Price']
        X = df.drop(['Price'],axis=1)
        return X,y


    def Train_Test_Split(self, X,y):
        X_train, X_test, y_train_true, y_test_true =train_test_split(X,y,test_size=.20,random_state=42)

        X_train.to_csv("G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//CleanedData//X_train.csv",index=False) 
        X_test.to_csv("G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//CleanedData//X_test.csv",index=False) 
        y_train_true.to_csv("G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//CleanedData//y_train_true.csv",index=False)  
        y_test_true.to_csv("G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//CleanedData//y_test_true.csv",index=False)

        print("-----------X_train-----------")
        print(X_train)







    def total_Stops(self, df):
            stop_mapping = {
                "non-stop": 0,
                "1 stop": 1,
                "2 stops": 2,
                "3 stops": 3,
                "4 stops": 4,
            }
            print("------Data TotalStops-------")

            print(df)
            df["Total_Stops"] = df["Total_Stops"].replace(stop_mapping)
            print("------Data TotalStops-------")

            return df


if __name__ == "__main__":
    cleaningObj = cleaning()
    df = cleaningObj.readData()
    df = cleaningObj.DataCleaning(df)
    df = cleaningObj.process_duration(df)
    df = cleaningObj.generate_Date_Time(df)
    df = cleaningObj.drop_unesseary_Col(df)
    print(df.shape)
    df = cleaningObj.remove_Outlier(df)
    X,y = cleaningObj.split_X_y(df)
    cleaningObj.Train_Test_Split(X,y)

    print(X)
    print(y)