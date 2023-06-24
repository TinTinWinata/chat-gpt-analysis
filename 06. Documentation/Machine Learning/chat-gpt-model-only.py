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