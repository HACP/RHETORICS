import time

from sklearn import svm, grid_search
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def svm_classifier(V_train, y_train, V_val, y_val, V_test, y_test):

    # Set the parameters by cross-validation
    parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                         'C': [1, 10, 100, 1000]},
                        {'kernel': ['linear'], 'C': [1, 10, 100, 1000], 'gamma' :[1,1.e-1,1.e-2,1.e-3,1.e-4]}]

    t0 = time.time()

    print 'Building SVM linear model'

    clf = svm.SVC(kernel='linear')
    
    #clf = grid_search.GridSearchCV(svm_clf, parameters)

    clf.fit(V_train, y_train)

    #print clf.best_params_

    t1 = time.time()
    print 'Building SVM linear model ... Done', str(int((t1 - t0)*100)/100.)
    print ''

    p_val =clf.predict(V_val)

    print 'Training accuracy on validation set', accuracy_score(y_val, p_val)

    p_test = clf.predict(V_test)

    #print 'Accuracy on testing set'

    #print classification_report(y_test, p_test)


def random_forest_classifier(V_train, y_train, V_val, y_val, V_test, y_test):

    t0 = time.time()

    print 'Building Random Forest model'

    clf = RandomForestClassifier(n_estimators=200)

    #clf = grid_search.GridSearchCV(svm_clf, parameters)                                                                                                                            

    clf.fit(V_train, y_train)

    #print clf.best_params_                                                                                                                                                         

    t1 = time.time()
    print 'Building Random Forest model ... Done', str(int((t1 - t0)*100)/100.)
    print ''

    p_val =clf.predict(V_val)

    print 'Training accuracy on validation set', accuracy_score(y_val, p_val)

    p_test = clf.predict(V_test)

    print 'Accuracy on testing set'                                                                                                                                                

    print classification_report(y_test, p_test)            


def sgd_classifier(V_train, y_train, V_val, y_val, V_test, y_test):

    t0 = time.time()

    print 'Building Random Forest model'

    clf = SGDClassifier(n_iter = 50)

    #clf = grid_search.GridSearchCV(svm_clf, parameters)                                                                                                                            

    clf.fit(V_train, y_train)

    #print clf.best_params_                                                                                                                                                         

    t1 = time.time()
    print 'Building Random Forest model ... Done', str(int((t1 - t0)*100)/100.)
    print ''

    p_val =clf.predict(V_val)

    print 'Training accuracy on validation set', accuracy_score(y_val, p_val)

    p_test = clf.predict(V_test)

    print 'Accuracy on testing set'

    print classification_report(y_test, p_test)
