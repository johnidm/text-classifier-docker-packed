import re
import stopwordsiso as stopwords


def clear(text):
    text = text.lower()
    text = re.sub(r"_+", "", text)
    text = re.sub(r"\b\d+\b", "", text)
    text = " ".join(
        [w for w in text.split() if not w in stopwords.stopwords("pt")])
    return text
