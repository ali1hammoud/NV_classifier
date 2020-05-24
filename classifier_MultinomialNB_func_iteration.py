import pandas as pd

def classifier_MultinomialNB_Avg(num):
    
    df=pd.read_csv("DATA.csv", usecols=['the_article', 'Class', 'label'])
    accuracy_value_list=[]
    for i in range(0, num):
        
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(df['the_article'], df['label'], test_size=0.2)

        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        X_train_cv = cv.fit_transform(X_train)
        X_test_cv = cv.transform(X_test)

        from sklearn.naive_bayes import MultinomialNB
        naive_bayes = MultinomialNB()
        naive_bayes.fit(X_train_cv, y_train)
        predictions = naive_bayes.predict(X_test_cv)

        from sklearn.metrics import accuracy_score, precision_score, recall_score
        accuracy_value_list.append(accuracy_score(y_test, predictions))

    avg = sum(accuracy_value_list) / len(accuracy_value_list)    
    return avg
