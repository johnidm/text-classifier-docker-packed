import numpy as np
import pickle
import config


def classify(text, threshold=0.7):
    with open(config.MODEL_FILE, 'rb') as f:
        model = pickle.load(f)

    texts = [text]
    predicts = np.array(model.predict_proba(texts)).flatten()

    targets = [
        target for target, prob in zip(model.classes_, predicts) if prob >= threshold
    ]

    return targets
