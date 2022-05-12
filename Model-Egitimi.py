 #Kütüphaneler
import matplotlib.pyplot
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import matplotlib as plt
warnings.filterwarnings('ignore')
# Gradient Boosting Classifier Model
from sklearn.ensemble import GradientBoostingClassifier
# Random Forest Classifier Model
from sklearn.ensemble import RandomForestClassifier
#LogisticRegression Model
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/phishing.csv")
test=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/train.csv")
#index sutunu silindi
data = data.drop(['Index'],axis = 1)
test = test.drop(['Index'],axis = 1)

#En son sutunda bulunan etiket kaldırıldı
X = data.drop(["class"],axis=1)
y = data["class"]

xt= test.drop(["class"],axis=1)
yt = test["class"]

#GradientBoostingClassifier modeli
gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)

#RandomForestClassifier Modeli
forest = RandomForestClassifier(n_estimators=10)

log = LogisticRegression()

#GradientBoostingClassifier model eğitimi
gbc.fit(X,y)

#RandomForestClassifier model eğitimi
forest.fit(X,y)

# fit the model 
log.fit(X,y)

#GradientBoostingClassifier tahmin sonuçları
y_train_gbc = gbc.predict(X)
y_test_gbc = gbc.predict(xt)

#RandomForestClassifier tahmin sonuçları
y_train_forest = forest.predict(X)
y_test_forest = forest.predict(xt)

y_train_log = log.predict(X)
y_test_log = log.predict(xt)

#Verilen egitim setinin phishing ve phishing olmayan site oranı
print("**********Eğitim Veri Setinin Oranlari*******************")
data['class'].value_counts().plot(kind='pie',autopct='%1.2f%%')
#plt.title("Phishing Count")
matplotlib.pyplot.title("phishing")
matplotlib.pyplot.show()

#Verilen test setinin phishing ve phishing olmayan site oranı
print("**********Test Veri Setinin Oranlari*******************")
test['class'].value_counts().plot(kind='pie',autopct='%1.2f%%')
#plt.title("Phishing Count")
matplotlib.pyplot.title("phishing")
matplotlib.pyplot.show()

print("****************Gradient Boosting Classifier******************")
acc_train_gbc = metrics.accuracy_score(y,y_train_gbc)
acc_test_gbc = metrics.accuracy_score(yt,y_test_gbc)
print("Gradient Boosting Classifier Egitim Accuracy  => {:.3f}".format(acc_train_gbc))
print("Gradient Boosting Classifier Test Accuracy => {:.3f}".format(acc_test_gbc))
print()
f1_score_train_gbc = metrics.f1_score(y,y_train_gbc)
f1_score_test_gbc = metrics.f1_score(yt,y_test_gbc)
print("Gradient Boosting Classifier Egitim f1_score  =>  {:.3f}".format(f1_score_train_gbc))
print("Gradient Boosting Classifier Test f1_score =>  {:.3f}".format(f1_score_test_gbc))
print()

recall_score_train_gbc = metrics.recall_score(y,y_train_gbc)
recall_score_test_gbc =  metrics.recall_score(yt,y_test_gbc)
print("Gradient Boosting Classifier Egitim Recall  =>  {:.3f}".format(recall_score_train_gbc))
print("Gradient Boosting Classifier Test Recall => {:.3f}".format(recall_score_test_gbc))
print()

precision_score_train_gbc = metrics.precision_score(y,y_train_gbc)
precision_score_test_gbc = metrics.precision_score(yt,y_test_gbc)
print("Gradient Boosting Classifier Egitim Precision  => {:.3f}".format(precision_score_train_gbc))
print("Gradient Boosting Classifier Test Precision  => {:.3f}".format(precision_score_test_gbc))
print("***************************************************************")
print("*****************RANDOM FOREST*********************************")
acc_train_forest = metrics.accuracy_score(y,y_train_forest)
acc_test_forest = metrics.accuracy_score(yt,y_test_forest)
print("Random Forest Egitim Accuracy  => {:.3f}".format(acc_train_forest))
print("Random Forest Test Accuracy => {:.3f}".format(acc_test_forest))
print()
f1_score_train_forest = metrics.f1_score(y,y_train_forest)
f1_score_test_forest = metrics.f1_score(yt,y_test_forest)
print("Random Forest Egitim f1_score  =>  {:.3f}".format(f1_score_train_forest))
print("Random Forest Test f1_score  => {:.3f}".format(f1_score_test_forest))
print()

recall_score_train_forest = metrics.recall_score(y,y_train_forest)
recall_score_test_forest = metrics.recall_score(yt,y_test_forest)
print("Random Forest Egitim Recall => {:.3f}".format(recall_score_train_forest))
print("Random Forest Test Recall => {:.3f}".format(recall_score_test_forest))
print()

precision_score_train_forest = metrics.precision_score(y,y_train_forest)
precision_score_test_forest = metrics.precision_score(yt,y_test_forest)
print("Random Forest Egitim Precision  => {:.3f}".format(precision_score_train_forest))
print("Random Forest Test Precision  => {:.3f}".format(precision_score_test_forest))
print("******************************************************")
print("**********************Logistic Regression***************************")
acc_train_log = metrics.accuracy_score(y,y_train_log)
acc_test_log = metrics.accuracy_score(yt,y_test_log)
print("Logistic Regression Egitim Accuracy  => {:.3f}".format(acc_train_log))
print("Logistic Regression Test Accuracy => {:.3f}".format(acc_test_log))
print()
f1_score_train_log = metrics.f1_score(y,y_train_log)
f1_score_test_log = metrics.f1_score(yt,y_test_log)
print("Logistic Regression Egitim f1_score  => {:.3f}".format(f1_score_train_log))
print("Logistic Regression Test f1_score  => {:.3f}".format(f1_score_test_log))
print()

recall_score_train_log = metrics.recall_score(y,y_train_log)
recall_score_test_log = metrics.recall_score(yt,y_test_log)
print("Logistic Regression Egitim Recall  => {:.3f}".format(recall_score_train_log))
print("Logistic Regression Test Recall  => {:.3f}".format(recall_score_test_log))
print()

precision_score_train_log = metrics.precision_score(y,y_train_log)
precision_score_test_log = metrics.precision_score(yt,y_test_log)
print("Logistic Regression Egitim Precision  => {:.3f}".format(precision_score_train_log))
print("Logistic Regression Test Precision  => {:.3f}".format(precision_score_test_log))

print("**********Gradient Boosting Classifier Test Ve Egitim Sonuclari****************")
training_accuracy = []
test_accuracy = []
#Modeli verilen derinlik kadar eğitimi
depth = range(1,10,1)
for n in depth:
    forest_test =  GradientBoostingClassifier(max_depth=n,learning_rate = 0.7)

    forest_test.fit(X, y)
    # Eğitim başarısı kaydet
    training_accuracy.append(forest_test.score(X, y))
    # Test Başarısı Kaydet
    test_accuracy.append(forest_test.score(xt, yt))
    
#plotting the eğitim & test başarı oranı goster
matplotlib.pyplot.figure(figsize=None)
matplotlib.pyplot.plot(depth, training_accuracy, label="Eğitim Başarısı")
matplotlib.pyplot.plot(depth, test_accuracy, label="Test Başarısı")
matplotlib.pyplot.ylabel("Başarı Oranı")  
matplotlib.pyplot.xlabel("Derinlik")
matplotlib.pyplot.legend();

print("**********Random Forest Classifier Test Ve Egitim Sonuclari****************")
training_accuracy = []
test_accuracy = []
#Modeli verilen derinlik kadar eğitimi
depth = range(1,10)
for n in depth:
    forest_test =  RandomForestClassifier(n_estimators=n)

    forest_test.fit(X, y)
    # Eğitim başarısı kaydet
    training_accuracy.append(forest_test.score(X,y))
    # Test Başarısı Kaydet
    test_accuracy.append(forest_test.score(xt, yt))
    

#plotting the eğitim & test başarı oranı goster
matplotlib.pyplot.figure(figsize=None)
matplotlib.pyplot.plot(depth, training_accuracy, label="Eğitim Başarısı")
matplotlib.pyplot.plot(depth, test_accuracy, label="Test Başarısı")
matplotlib.pyplot.ylabel("Başarı Oranı")  
matplotlib.pyplot.xlabel("Derinlik")
matplotlib.pyplot.legend();

print("**********Lojistik Regresyon Classifier Test Ve Egitim Sonuclari****************")
training_accuracy = []
test_accuracy = []
#Modeli verilen derinlik kadar eğitimi
depth = range(1,10)
for n in depth:
    logr =  LogisticRegression(max_iter=n)

    logr.fit(X, y)
    # Eğitim başarısı kaydet
    training_accuracy.append(logr.score(X,y))
    # Test Başarısı Kaydet
    test_accuracy.append(logr.score(xt, yt))
    

#plotting the eğitim & test başarı oranı goster
matplotlib.pyplot.figure(figsize=None)
matplotlib.pyplot.plot(depth, training_accuracy, label="Eğitim Başarısı")
matplotlib.pyplot.plot(depth, test_accuracy, label="Test Başarısı")
matplotlib.pyplot.ylabel("Başarı Oranı")  
matplotlib.pyplot.xlabel("Derinlik")
matplotlib.pyplot.legend();
matplotlib.pyplot.figure(figsize=(9,7))
n_features = X.shape[1]
matplotlib.pyplot.barh(range(n_features), gbc.feature_importances_, align='center')
matplotlib.pyplot.yticks(np.arange(n_features), X.columns)
matplotlib.pyplot.title("Özelliklerin Sonuca Etkileri")
matplotlib.pyplot.xlabel("Özellik Ağırlık Oranı")
matplotlib.pyplot.ylabel("Özellikler")
matplotlib.pyplot.show()
