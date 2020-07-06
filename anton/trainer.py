import pickle
import re
import config

from anton.cleaner import clear

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer


def train():
    df = pd.read_csv(config.DATASET_FILE)
    
    X, y = df.text, df.label
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    pipe = Pipeline([('tfidf', TfidfVectorizer(preprocessor=clear,
                                               min_df=5)),
                     ('clf', CalibratedClassifierCV(LinearSVC())),
                     ], verbose=True)

    pipe.fit(X_train, y_train)

    with open(config.MODEL_FILE, 'wb') as f:
        pickle.dump(pipe, f)
