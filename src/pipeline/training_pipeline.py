from src.components.Step_01_Data_cleaning import Cleaning

if __name__ =='__main__':
    cleaning_obj = Cleaning()
    df = cleaning_obj.read_data(filepath = 'G://Ethans//ML//Projects//Final Projects//Airline-Prediction-End-to-End//Artifact//Data//Airline1.csv')
    print(df)