# Naive Bayes

# Importing the libraries
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn import metrics
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
        self.draw_cm_matrix()

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

    def split_dataset(self):
        # TODO: Split the self.X & self.y (dataset) into Training data and Test data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.25, random_state=0)

    def feature_scaling(self):
        # TODO: Make a Feature Scaling for the training
        self.X_train = self.sc.fit_transform(self.X_train)

    def training_dataset(self):
        # TODO: Training the train data with Naive Bayes Algorithm to make the model
        self.classifier = GaussianNB()
        self.classifier.fit(self.X_train, self.y_train)

    def test_result(self):
        # TODO: Print the Confusion Matrix and make a prediction accurate percentage based on the model on training_dataset method
        self.X_test = self.sc.transform(self.X_test)
        y_pred = self.classifier.predict(self.X_test)
        self.cm = confusion_matrix(self.y_test, y_pred)
        accuracy = accuracy_score(self.y_test, y_pred)
        print("Confusion Matrix:")
        print(self.cm)
        print("Prediction Accuracy:", accuracy)

    def predict_data(self):
        # TODO: Predict the self.data input from the user based on the created modoel
        data_scaled = self.sc.transform([self.data])
        prediction = self.classifier.predict(data_scaled)
        if prediction[0] == 1:
            print("The user is predicted to have diabetes.")
        else:
            print("The user is predicted to not have diabetes.")

    def draw_cm_matrix(self):
        cm_display = metrics.ConfusionMatrixDisplay(
            confusion_matrix=self.cm, display_labels=[False, True])
        cm_display.plot()
        plt.show()


gender = 1
age = 19
hypertension = 0
heart_disease = 0
smoking_history = 0
bmi = 24.2
HbA1c_level = 5
blood_glucose_level = 130

data = [gender, age, hypertension, heart_disease,
        smoking_history, bmi, HbA1c_level, blood_glucose_level]

model = NaiveBeyes(file_name='diabetes_data.csv', data=data)
