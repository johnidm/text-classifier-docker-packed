FROM python:3.8-slim

WORKDIR /app

RUN pip install --no-cache-dir \ 
            numpy \
            matplotlib \
            scipy \
            scikit-learn \
            pandas \ 
            stopwordsiso \
            flask

COPY . .

ARG LANG_CODE=
RUN echo "Training the classifier with language code: '${LANG_CODE}'"

RUN python train.py

CMD ["python", "app.py"]
