# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:59:59 2023

@author: Shaina Mehta
"""

from typing import Optional
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:
    
    def data_characteristics(self,dataset: pd.DataFrame,  info: Optional[bool] = False) -> GeneratorExit:
        yield f'Datset Shape: {dataset.shape}'
        yield f'Dataset features: {dataset.columns.values}'
        if info:
            yield f'Dataset Info: {dataset.info()}'
        yield f'Dataset types: {dataset.dtypes}'
        yield dataset.describe().T
        yield f'Null Values in Dataset: {dataset.isnull().sum()}'
        
    def unique_values(self,dataset: pd.DataFrame) -> GeneratorExit:
        for column in dataset.columns:
            yield f'Unique Value in {column} :\n{dataset[column].unique()}'
    
    def target_distribution(self, dataset: pd.DataFrame, target: str) -> 'plot':
        sns.displot(data, x=target, kind="kde", bw_adjust=2)
        plt.xlabel(target)
        plt.ylabel('Count')
        plt.title('Target Regression Distribution')
        plt.show()
    
    def histoplots(cls, dataset: pd.DataFrame, numeric_features: list[str]) -> 'plot':
        dataset.hist(numeric_features, figsize = (15, 8))
        plt.show()


class DataPreprocessing:
    
    def int_to_float(self, dataset: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
        for col in cols:
            dataset[col] = dataset[col].astype(float)
        return dataset
    
    def correlation_matrix(self, dataset:pd.DataFrame) -> 'plot':
        cm = dataset.corr().round(2)
        sns.heatmap(data=cm,annot=True, cmap='Blues_r')
        plt.title('Correlation Matrix of The Features and the Target Values')
        plt.show()
        
    def segregate_features_and_target(self, dataset:pd.DataFrame) -> tuple:
        X = dataset.iloc[:,:4].values
        Y = dataset.iloc[:,4:].values
        return (X,Y)
    
    
class MLModel:
    def metrics(self, y_test: np.ndarray, y_pred: np.ndarray) -> None:
        #acc: float = model.score(x_test,y_test)
        mse: float = mean_squared_error(y_test,y_pred) 
        mae: float = mean_absolute_error(y_test,y_pred)
        r2: float = r2_score(y_test,y_pred)
        print(f'Mean Squared Error: {mse}')
        print(f'Mean Absolute Error: {mae}')
        print(f'Coefficient of Determination: {r2}')
    
    def linear_regression(self, x_train, x_test, y_train, y_test) -> None:
        model = LinearRegression()
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        print(f'For ALE:')
        self.metrics(y_test[:,0], y_pred[:,0])
        print(f'For SD ALE:')
        self.metrics(y_test[:,1], y_pred[:,1])

if __name__ == "__main__":
    
    #Loading the dataset
    data = pd.read_csv("C:\\Users\\Shaina Mehta\\.spyder-py3\\dataale.csv")     
    data_characteristic = DataAnalysis().data_characteristics(data)
    while True:
        try:
            print('-'*100)
            print(data_characteristic.__next__())
        except StopIteration: break
    
    #Data Analysis
    DataAnalysis().target_distribution(data, 'ale')
    DataAnalysis().target_distribution(data, 'sd_ale')
    DataAnalysis().histoplots(data, numeric_features = ['anchor_ratio', 'trans_range', 'node_density', 'iterations'])
    
    #Data Pre-processing
    data = DataPreprocessing().int_to_float(data, cols = ['anchor_ratio', 'trans_range', 'node_density', 'iterations'])
    DataPreprocessing().correlation_matrix(data)
    
    #ML Model
    X, Y = DataPreprocessing().segregate_features_and_target(data)
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    #print(type(x_train), type(x_test), type(y_train), type(y_test))
    MLModel().linear_regression(x_train, x_test, y_train, y_test)
    