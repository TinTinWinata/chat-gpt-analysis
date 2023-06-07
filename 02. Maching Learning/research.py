# Naive Bayes

# Importing the libraries
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


class SmokingHistory(Enum):
    NOINFO = 'No Info'
    NEVER = 'never'
    CURRENT = 'current'
    FORMER = 'former'
    NOTCURRENT = 'not current'
    EVER = 'ever'

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class NaiveBeyes():

    def __init__(self, file_name, data):
        self.data = data
        self.sc = StandardScaler()
        self.load_dataset(file_name=file_name)
        self.split_dataset()
        self.feature_scaling()
        self.training_dataset()
        self.test_result()

    def load_dataset(self, file_name):
        # Importing the dataset
        self.dataset = pd.read_csv(file_name)
        self.X = self.dataset.iloc[:, :-1].values
        self.y = self.dataset.iloc[:, -1].values
        for item in self.X:

            # Changing Gender
            if item[0] == Gender.FEMALE.value:
                item[0] = 0
            else:
                item[0] = 1

            # Changing Smoking History
            if item[4] == SmokingHistory.NOINFO.value:
                item[4] = 0
            elif item[4] == SmokingHistory.NEVER.value:
                item[4] = 1
            elif item[4] == SmokingHistory.FORMER.value:
                item[4] = 2
            elif item[4] == SmokingHistory.CURRENT.value:
                item[4] = 3
            elif item[4] == SmokingHistory.NOTCURRENT.value:
                item[4] = 4
            elif item[4] == SmokingHistory.EVER.value:
                item[4] = 5
            else:
                print(f'Unknown Value : {item[4]}')
        # print('X : ', self.X)
        # print('Y : ', self.y)

    def split_dataset(self):
        # Splitting the dataset into the Training set and Test set
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.25, random_state=0)
        # print('X Train : ', self.X_train)
        # print('Y Train : ', self.y_train)
        # print('X Test : ',self.X_test)
        # print('Y Test : ', self.y_test)

    def feature_scaling(self):
        # Feature Scaling
        self.X_train = self.sc.fit_transform(self.X_train)
        self.X_test = self.sc.transform(self.X_test)
        # print(self.X_train)
        # print(self.X_test)

    def training_dataset(self):
        # Training the Naive Bayes model on the Training set
        classifier = GaussianNB()
        classifier.fit(self.X_train, self.y_train)

        # Predicting a new result
        result = classifier.predict(self.sc.transform([self.data]))
        print('Predict Result : ', result)
        if result == 0:
            print('You are not diabetes!')
        else:
            print('You are diabetes!')

        # Predicting the Test set results
        self.y_pred = classifier.predict(self.X_test)
        # print(np.concatenate((self.y_pred.reshape(len(self.y_pred), 1),
        #       self.y_test.reshape(len(self.y_test), 1)), 1))

    def test_result(self):    swasw
        # Making the Confusion Matrix
        cm = confusion_matrix(self.y_test, self.y_pred)
        print('Confusion Matrix : ', cm)
        score = accuracy_score(self.y_test, self.y_pred)
        print('Accuracy score : ', score)

gender = 1 
age = 19
hypertension = 0
heart_disease =  0
smoking_history = 0
bmi = 24.2
HbA1c_level = 5
blood_glucose_level = 130 

data = [gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]

model = NaiveBeyes(file_name='diabetes_data.csv', data=data)
