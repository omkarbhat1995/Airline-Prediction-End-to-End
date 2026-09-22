import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (RandomForestRegressor,GradientBoostingRegressor)
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from sklearn.model_selection import GridSearchCV
import joblib

import numpy as np

class Training:
    def __init__(self):
        self.models = {
            "Linear_Reg": LinearRegression(),
            "Ridge_Reg": Ridge(),
            "Lasso_Reg": Lasso(),
            "Elastic_Net": ElasticNet(),
            "S_Vector_Reg": SVR(),
            "Decision_Tree_Reg": DecisionTreeRegressor(),
            "Random_Forest_Reg": RandomForestRegressor(),
            "Gradient_Boosting_Reg": GradientBoostingRegressor()
        }

        self.params = {
            "Linear_Reg": {},
            "Ridge_Reg": {"alpha": [0.1, 1.0, 10.0]},
            "Lasso_Reg": {"alpha": [0.01, 0.1, 1.0]},
            "Elastic_Net": {"alpha": [0.01, 0.1, 1.0]},
            "S_Vector_Reg": {"C": [0.1, 1, 10]},
            "Decision_Tree_Reg": {"max_depth": [3, 5, 10]},
            "Random_Forest_Reg": {"n_estimators": [50, 100, 200]},
            "Gradient_Boosting_Reg": {"learning_rate": [0.01, 0.1, 0.2]}}

    def read_Data(self):
        X_test = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\X_test.csv")
        X_train = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\X_train.csv")
        y_test_true = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\y_test_true.csv")
        y_train_true = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\CleanedData\\y_train_true.csv")

        X_train_trans = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\Trans_data\\X_train_trans.csv")
        X_test_trans = pd.read_csv("G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\Data\\Trans_data\\X_test_trans.csv")
        return X_test,X_train,y_test_true,y_train_true,X_train_trans,X_test_trans

    def linear_Metrics(self,x_Data,True_Value,Pred_Value):
        MSE = mean_squared_error(True_Value,Pred_Value) 
        MAE = mean_absolute_error(True_Value,Pred_Value)
        RMSE = np.sqrt(MSE)
        R2 = r2_score(True_Value,Pred_Value)

        n = len(x_Data)
        p = x_Data.shape[1]
        A_R2 = 1-(1-R2)*(n-1)/(n-p-1)

        merticsDict = {"MSE": MSE,"MAE":MAE,"RMSE": RMSE,"R2": R2,"A_R2":A_R2}

        print(merticsDict)
        return merticsDict

    def ModelTraining(self,X_train,X_train_trans,y_train_true):
        EvaluationDict = {}

        print("X_train shape       :", X_train.shape)
        print("X_train_trans shape :", X_train_trans.shape)
        print("y_train_true shape  :", y_train_true.shape)

        for Model_Name,Model in self.models.items():
            grid_search = GridSearchCV(Model, self.params[Model_Name], cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train_trans, y_train_true)

            best_model_instance = grid_search.best_estimator_
            y_train_pred = best_model_instance.predict(X_train_trans)
            joblib.dump(best_model_instance,f"G:\\Ethans\\ML\\Projects\\Final Projects\\Airline-Prediction-End-to-End\\Artifact\\model_files\\{Model_Name}.pkl")
            print(Model_Name)
            Metrics_v = self.linear_Metrics(X_train,y_train_true,y_train_pred)
            EvaluationDict[Model_Name] = Metrics_v

        print("----------------------------")
        print(EvaluationDict)
        for key,value in EvaluationDict.items():
            print(key,value)