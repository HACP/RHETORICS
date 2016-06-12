import DPlib, MLlib

X_train, y_train, X_val, y_val, X_test, y_test = DPlib.get_data()

#V_train, V_val, V_test = DPlib.Vectorize(X_train, X_val, X_test)

min_df_l = [2,3,4,5,6]
max_df_l = [0.5, 0.6, 0.7, 0.8]

for min_df in min_df_l:
    for max_df in max_df_l:

        print 'min_df', min_df, 'max_df',max_df

        V_train, V_val, V_test = DPlib.Vectorize(X_train, X_val, X_test, min_df, max_df)
        #MLlib.svm_classifier(V_train, y_train, V_val, y_val, V_test, y_test)
        #MLlib.random_forest_classifier(V_train, y_train, V_val, y_val, V_test, y_test)
        MLlib.sgd_classifier(V_train, y_train, V_val, y_val, V_test, y_test)
