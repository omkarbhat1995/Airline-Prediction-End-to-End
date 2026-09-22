from src.components.Step_01_Cleaning import cleaning
from src.components.Step_02_Transformation import transformation
from src.components.Step_03_Training import Training

if __name__ == "__main__":
    cleaningObj = cleaning()
    df = cleaningObj.readData()
    df = cleaningObj.DataCleaning(df)
    df = cleaningObj.process_duration(df)
    df = cleaningObj.generate_Date_Time(df)
    df = cleaningObj.drop_unesseary_Col(df)
    df = cleaningObj.remove_Outlier(df)
    X,Y = cleaningObj.split_X_y(df)
    cleaningObj.Train_Test_Split(X,Y)

    TranObj = transformation()
    X_train,X_test = TranObj.read_Data()
    transform_Obj = TranObj.ColumnTransform()
    TranObj.encoding(transform_Obj,X_train,X_test)

    TrainObj = Training()
    X_test,X_train,y_test_true,y_train_true,X_train_trans,X_test_trans = TrainObj.read_Data()
    TrainObj.ModelTraining(X_train,X_train_trans,y_train_true)