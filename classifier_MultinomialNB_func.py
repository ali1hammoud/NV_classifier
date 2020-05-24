#pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation
#Seaborn is a Python data visualization library based on matplotlib.
#It provides a high-level interface for drawing attractive and informative statistical graphics.
#we use it to draw the heatmap of the result
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import nv_ali
def classifier_MultinomialNB():
    df=pd.read_csv("DATA.csv", usecols=['the_article', 'Class', 'label'])

    from sklearn.model_selection import train_test_split
    #split data and target into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['the_article'], df['label'], test_size=0.2)

    from sklearn.feature_extraction.text import CountVectorizer
    #instantiate the vectorizer
    cv = CountVectorizer()
    #fit and transform training data into a document-term matrix
    X_train_cv = cv.fit_transform(X_train)
    #transform testing data into a document-term matrix
    X_test_cv = cv.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    #instantiate a Multinomial Naive Bayes model
    naive_bayes = MultinomialNB()
    #Fit Naive Bayes classifier according to X_train_cv, y_train
    naive_bayes.fit(X_train_cv, y_train)
    #Perform classification on an array of test vectors X_test_cv.
    predictions = naive_bayes.predict(X_test_cv)
    
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    #calculate accuracy of predictions
    accuracy_value=accuracy_score(y_test, predictions)
##    print('Accuracy score: ', accuracy_score(y_test, predictions))
##    print('Precision score: ', precision_score(y_test, predictions))
##    print('Recall score: ', recall_score(y_test, predictions))

    
    from sklearn.metrics import confusion_matrix 
    cm = confusion_matrix(y_test, predictions) 
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax)
    # labels, title and ticks
    ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels')
    ax.set_title('The accuracy of this predictions is '+str(accuracy_value))
    ax.xaxis.set_ticklabels(['Art', 'Science']); ax.yaxis.set_ticklabels(['Art', 'Science'])
    plt.show()
