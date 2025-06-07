import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def readCSV():
    df = pd.read_csv('addiction_population_data.csv')
    df = df[df['gender'].isin(['Male', 'Female'])]
    return df

def createVisualization(data, name):
    plt.figure(figsize=(10,6))
    plt.scatter(data[data['gender']=='Male']['age'], data[data['gender']=='Male']['bmi'], label='Male', alpha=0.7)
    plt.scatter(data[data['gender']=='Female']['age'], data[data['gender']=='Female']['bmi'], label='Female', alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.legend()
    plt.title(name + ' set: Age vs BMI')
    plt.show()


def createHistogram(data, name):
    for col in ['age', 'bmi']:
        plt.hist(data[col], bins=20, alpha=0.5, label='All')
        plt.hist(data[data['gender']=='Male'][col], bins=20, alpha=0.5, label='Male')
        plt.hist(data[data['gender']=='Female'][col], bins=20, alpha=0.5, label='Female')
        plt.title(name + f' Распределение по {col}')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    df = readCSV()
    # Выборка по гендеру по 100 человек
    train, test = train_test_split(df, test_size=0.0505, train_size=0.051, stratify=df['gender'], random_state=42)

    train = train[(train['bmi'] > 10) & (train['bmi'] < 60) & (train['age'] > 10) & (train['age'] < 100)]
    test = test[(test['bmi'] > 10) & (test['bmi'] < 60) & (test['age'] > 10) & (test['age'] < 100)]
    
    createVisualization(train, 'Train')
    createVisualization(test, 'Test')

    createHistogram(train, 'Train')
    createHistogram(test, 'Test')