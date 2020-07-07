import pickle
import re
import config

from anton.cleaner import clear
from anton import plotters

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def train():
    df = pd.read_csv(config.DATASET_FILE)

    X, y = df.text, df.label
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    pipe = Pipeline([('tfidf', TfidfVectorizer(preprocessor=clear,
                                               min_df=5)),
                     ('clf', CalibratedClassifierCV(LinearSVC())),
                     ], verbose=True)

    pipe.fit(X_train, y_train)

    print(f"Saving classifier in {config.MODEL_FILE}")
    with open(config.MODEL_FILE, 'wb') as f:
        pickle.dump(pipe, f)

    y_predict = pipe.predict(X_test)

    print("------")
    print("accuracy:", accuracy_score(y_test, y_predict))
    print(classification_report(y_test, y_predict))
    print(confusion_matrix(y_test, y_predict))
    print(df.groupby("label").count())
    print("------")

    print("Save the plotters")
    plotters.save_all(df)
