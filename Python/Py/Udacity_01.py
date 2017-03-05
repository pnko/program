import numpy
import pandas
import statsmodels.api as sm

file_path = "data/titanic-data.csv"
df = pandas.read_csv(file_path)

def simple_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' :
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions


a= simple_heuristic(file_path =file_path)

print(sum(df['Survived']))
print(sum(a.values()))
print(sum(a.values())/sum(df['Survived']))
print("="*30)

def complex_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' and passenger['Pclass'] == 1 and  passenger['Age'] <= 18 :
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions



b=complex_heuristic(file_path =file_path)
print(sum(df['Survived']))
print(sum(b.values()))
print(sum(b.values())/sum(df['Survived']))