# Naive Bayes

# Importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


class NaiveBeyes():

    def __init__(self, file_name):
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

    def split_dataset(self):
        # Splitting the dataset into the Training set and Test set
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.25, random_state=0)
        print(self.X_train)
        print(self.y_train)
        print(self.X_test)
        print(self.y_test)

    def feature_scaling(self):
        # Feature Scaling
        self.X_train = self.sc.fit_transform(self.X_train)
        self.X_test = self.sc.transform(self.X_test)
        print(self.X_train)
        print(self.X_test)

    def training_dataset(self):
        # Training the Naive Bayes model on the Training set
        classifier = GaussianNB()
        classifier.fit(self.X_train, self.y_train)

        # Predicting a new result
        print(classifier.predict(self.sc.transform([[30, 87000]])))

        # Predicting the Test set results
        self.y_pred = classifier.predict(self.X_test)
        print(np.concatenate((self.y_pred.reshape(len(self.y_pred), 1),
              self.y_test.reshape(len(self.y_test), 1)), 1))

    def test_result(self):
        # Making the Confusion Matrix
        cm = confusion_matrix(self.y_test, self.y_pred)
        print('Confusion Matrix : ', cm)
        score = accuracy_score(self.y_test, self.y_pred)
        print('Accuracy score : ', score)


model = NaiveBeyes(file_name='Social_Network_Ads.csv')
