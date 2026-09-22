from src.components.Step_01_Cleaning import cleaning
from src.components.Step_02_Transformation import transformation
if __name__ == "__main___":
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

    trans_obj = transformation()
    X_train, X_test = trans_obj.read_data()
    transformation_obj = trans_obj.Column_transform()
    trans_obj.encoding(transformation_obj)