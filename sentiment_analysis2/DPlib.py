import time

import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def get_data():

    t0 = time.time()

    print 'Loading data ... Start'

    data = pd.read_csv('../data/Tweets.csv')

    X = data['text']
    tY = data['airline_sentiment']


    lY = []
    for item in tY:
        if item == 'positive':
            lY.append(1)
        if item == 'negative':
            lY.append(-1)
        if item == 'neutral':
            lY.append(0)

    y = np.array(lY)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

    t1 = time.time()


    print 'Loading data ... Done', str(int((t1 - t0)*100)/100.)
    print ''

    print 'Testing set', len(X_test)
    print 'Validation set', len(X_val)
    print 'Training set', len(X_train)

    print ''

    return X_train, y_train, X_val, y_val, X_test, y_test


def Vectorize(X_train, X_val, X_test, min_df=4,max_df=0.8):
    t0 = time.time()

    print 'Vectorization ... Start'

    vectorizer = TfidfVectorizer(min_df=min_df,
                                 max_df=max_df,
                                 sublinear_tf=True,
                                 use_idf=True)
    V_train = vectorizer.fit_transform(X_train)
    V_val = vectorizer.transform(X_val)
    V_test = vectorizer.transform(X_test)
    
    t1 = time.time()
    
    print 'Vectorization data ... Done', str(int((t1 - t0)*100)/100.)
    print ''

    print 'Number of train features', V_train.shape
    
    return V_train, V_val, V_test
