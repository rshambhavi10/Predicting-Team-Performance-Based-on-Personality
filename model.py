
import matplotlib.pyplot as plt
#import pandas as pd
import pickle
import pandas 
import numpy 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 

  
teams = pandas.read_csv('data_new_1.csv')     


'''
#np.random.seed(3)
le = preprocessing.LabelEncoder()
teams = teams.apply(le.fit_transform)
'''

y = teams.isEff
X = teams.drop('isEff',axis=1)

    # Store the names of the selected columns
feature_names = X.columns
    
'''
    # Feature selection
    sel_chi2 = SelectKBest(score_func = mutual_info_classif, k=i)    
    sel_chi2.fit_transform(X, y)
    col_num = sel_chi2.get_support(indices = True)

    # Retaining only the selected K columns
    X = X.iloc[:,col_num]
'''
    
    
    # After the feature selection, split the data into train and test
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.20, random_state = 1)

 
'''

   params = {
                'train_X': train_X,
                'test_X': test_X,
                'train_y': train_y,
                'test_y': test_y,
                'feature_names' : feature_names
                 
             }



def model_building(params,depth):
    
    train_X = params['train_X']
    train_y = params['train_y']
    test_X = params['test_X']
    test_y = params['test_y']


'''

    
    # Apply Decision Tree Model and predict on the test set

dt = DecisionTreeClassifier(criterion='gini', random_state = 1, max_depth=5, min_samples_split = 10)
dt.fit(train_X,train_y)
pred = dt.predict(test_X) 


print ("Desicion Tree Accuracy is ", 
             accuracy_score(test_y, pred)*100 ) 


# Saving model to disk
pickle.dump(dt, open('model12.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model12.pkl','rb'))

x=[[4,0,0,0,0,1,0,0,0,1]]
print(model.predict(x))


    

