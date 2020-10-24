import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


class Model:

    def __init__(self):
        self.name = ''
        path = 'dataset/kidney_disease.csv'
        df = pd.read_csv(path)
        df = df[['age', 'bp', 'su', 'pc', 'pcc', 'sod', 'hemo', 'htn', 'dm', 'classification']]

        df['age'] = df['age'].fillna(df['age'].mean())
        df['bp'] = df['bp'].fillna(df['bp'].mean())
        df['su'] = df['su'].fillna(df['su'].mode()[0])
        df['pc'] = df['pc'].fillna(df['pc'].mode()[0])
        df['pcc'] = df['pcc'].fillna(df['pcc'].mode()[0])
        df['sod'] = df['sod'].fillna(df['sod'].mode()[0])
        df['hemo'] = df['hemo'].fillna(df['hemo'].mode()[0])
        df['htn'] = df['htn'].fillna(df['htn'].mode()[0])
        df['dm'] = df['dm'].str.replace(" ", "")
        df['dm'] = df['dm'].str.replace("\t", "")
        df['dm'] = df['dm'].fillna(df['dm'].mode()[0])
        df['classification'] = df['classification'].str.replace("\t", "")
        df['classification'] = df['classification'].fillna(df['classification'].mode()[0])

        labelencoder = LabelEncoder()
        df['pc'] = labelencoder.fit_transform(df['pc'])
        df['pcc'] = labelencoder.fit_transform(df['pcc'])
        df['htn'] = labelencoder.fit_transform(df['htn'])
        df['dm'] = labelencoder.fit_transform(df['dm'])
        df['classification'] = labelencoder.fit_transform(df['classification'])
        self.split_data(df)

    def split_data(self,df):
        x = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
        y = df.iloc[:, 9].values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=24)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def svm_classifier(self):
        self.name = 'Svm Classifier'
        classifier = SVC()
        return classifier.fit(self.x_train, self.y_train)

    def decisionTree_classifier(self):
        self.name = 'Decision tree Classifier'
        classifier = DecisionTreeClassifier()
        return classifier.fit(self.x_train,self.y_train)


    def randomforest_classifier(self):
        self.name = 'Random Forest Classifier'
        classifier = RandomForestClassifier()
        return classifier.fit(self.x_train,self.y_train)

    def naiveBayes_classifier(self):
        self.name = 'Naive Bayes Classifier'
        classifier = GaussianNB()
        return classifier.fit(self.x_train,self.y_train)


    def knn_classifier(self):
        self.name = 'Knn Classifier'
        classifier = KNeighborsClassifier()
        return classifier.fit(self.x_train,self.y_train)


    def accuracy(self,model):
        predictions = model.predict(self.x_test)
        cm = confusion_matrix(self.y_test, predictions)
        accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
        print(f"{self.name} has accuracy of {accuracy *100} % ")

if __name__ == '__main__':
    model = Model()
    model.accuracy(model.svm_classifier())
    model.accuracy(model.decisionTree_classifier())
    model.accuracy(model.randomforest_classifier())
    model.accuracy(model.naiveBayes_classifier())
    model.accuracy(model.knn_classifier())
