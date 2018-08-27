
import time 
import pandas as pd                                                                                                                                
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
    
print("read_csv..............."+ time.asctime())
df_train = pd.read_csv('./train_set.csv')
df_test = pd.read_csv('./test_set.csv')
df_train.drop(columns=['article','id'], inplace=True)
df_test.drop(columns=['article'], inplace=True)

print("CountVectorizer..............."+ time.asctime())
vectorizer = CountVectorizer(ngram_range=(1,2), min_df=3, max_df=0.9, max_features=100000)
vectorizer.fit(df_train['word_seg'])
x_train = vectorizer.transform(df_train['word_seg'])
x_test = vectorizer.transform(df_test['word_seg'])
y_train = df_train['class']-1

print("LogisticRegression..............."+ time.asctime())
lg = LogisticRegression(C=4, dual=True)
lg.fit(x_train, y_train)

print("predict..............."+ time.asctime())
y_test = lg.predict(x_test)

df_test['class'] = y_test.tolist()
df_test['class'] = df_test['class'] + 1
print("result_to_csv..............."+ time.asctime())
df_result = df_test.loc[:, ['id', 'class']]
df_result.to_csv('./result.csv', index=False)

print("finish...............")