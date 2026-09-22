import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler



class transformation:
    def __init__(self):
        pass

    def read_Data(self):
        X_train = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\X_train.csv")
        X_test = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\X_test.csv")
        return X_train, X_test
    def ColumnTransform(self):
        numericalCol = ['Total_Stops','DurHrs_Mins','D_Day','D_Month','D_Year','D_Hour','D_Minute','A_Hour','A_Minute','A_Day','A_Month','A_Year']
        OneHotCol =['Airline','Source','Destination'] 

        OneHotEncoding_01 =  ("One_Hot_Encoder",OneHotEncoder(sparse_output=False, drop="first", handle_unknown="ignore"),OneHotCol,)
        Scaling = ("Numerical_Coluns", StandardScaler(), numericalCol)
        transform_Obj = ColumnTransformer(transformers=[OneHotEncoding_01,Scaling]).set_output(transform="pandas")
        return transform_Obj

    def encoding(self,transform_Obj,X_train,X_test):
        X_train_trans = transform_Obj.fit_transform(X_train)
        joblib.dump(transform_Obj,"G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\trans_files\\Transform.pkl")
        transFile = joblib.load("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\trans_files\\Transform.pkl")

        X_train_trans.to_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\Trans_data\\X_Train_Trans.csv",index=False)
        X_test_trans = transFile.fit_transform(X_test)
        X_test_trans.to_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\Trans_data\\X_Test_Trans.csv",index=False)