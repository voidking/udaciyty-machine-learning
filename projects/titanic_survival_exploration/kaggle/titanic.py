# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

# Load the dataset 
# 加载数据集
in_file = 'test.csv'
full_data = pd.read_csv(in_file)


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    # 确保预测的数量与结果的数量一致
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        # 计算预测准确率（百分比）
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"
    
# Test the 'accuracy_score' function
# 测试 'accuracy_score' 函数
# predictions = pd.Series(np.ones(5, dtype = int))
# print accuracy_score(outcomes[:5], predictions)

def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        if passenger['Sex'] == 'female' and (passenger['Pclass'] == 1 or passenger['Pclass'] == 2):
            predictions.append(1)
        elif passenger['Sex'] == 'female' and passenger['Pclass'] == 3 and (passenger['Age'] < 40 or passenger['Age'] > 50) and passenger['SibSp'] == 0:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10 and (passenger['Pclass'] == 1 or passenger['Pclass'] == 2):
            predictions.append(1)
        elif passenger['Fare'] > 400:
            predictions.append(1)
        else:
            predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
# predictions = predictions_3(data)

# print accuracy_score(outcomes, predictions)

def print_csv(data):
    passenger_arr = []
    survive_arr = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        passenger_arr.append(passenger['PassengerId'])
        if passenger['Sex'] == 'female' and (passenger['Pclass'] == 1 or passenger['Pclass'] == 2):
            survive_arr.append(1)
        elif passenger['Sex'] == 'female' and passenger['Pclass'] == 3 and (passenger['Age'] < 40 or passenger['Age'] > 50) and passenger['SibSp'] == 0:
            survive_arr.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10 and (passenger['Pclass'] == 1 or passenger['Pclass'] == 2):
            survive_arr.append(1)
        elif passenger['Fare'] > 400:
            survive_arr.append(1)
        else:
            survive_arr.append(0)
    result = {'PassengerId': passenger_arr,'Survived': survive_arr}
    pf = pd.DataFrame(result)
    # pf有索引，没有找到去掉的函数，暂时手动处理
    out_file = 'output.csv'
    pf.to_csv(out_file)

print_csv(full_data)




