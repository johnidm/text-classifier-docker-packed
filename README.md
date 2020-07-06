# A minimalist text classifier packed in a Docker image

The goal of this project is to build a Docker image to train a text classifier and provide a REST API to consume the trained model.

Feel free to use the main idea of this project and adapt it for your own purposes. The core concept here is simplicity.

## Steps to build your own text classification project

### 1) Create the dataset

- The trainer expects data to be arranged as CSV records in a file named `dataset.csv`.

- This file is going to be read and processed when the Docker image is built.

- Below is an example of what `dataset.csv` might look like.

```csv
label,text
tec,tv future in the hands of viewers with home th...
business,worldcom boss left books alone former worldc...
sport,tigers wary of farrell gamble leicester say ...
sport,yeading face newcastle in fa cup premiership s...
entertainment, ocean s twelve raids box office ocean s twelve...
...
```

- In the the above example, the column **label** gives the classification for the associated **text**.

### 2) Build and run the Docker image

- If you wish to have stopwords removed from the training data, make sure to provide the correponding language code (see `LANG_CODE` in the examples below). Refer to https://github.com/stopwords-iso/stopwords-iso#list-of-included-languages for a list of valid values.

No stopword removal:

```bash
docker build -t anton:v1 .
```

Stopword removal for the Portuguese language:

```bash
docker build --build-arg LANG_CODE=pt -t anton:v1 .
```

- After the image has been built, you may start the container:

```bash
docker container run -e LANG_CODE=pt --rm -it -p 5000:5000 anton:v1
```

Notice that, if `LANG_CODE` was specified as a `build-arg` when building the Docker image, it should also be provided as an environment variable when launching a container. Also, make sure the language codes match.

- Sample request:

```bash
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "threshold": 0.4,
  "text": "souness delight at euro..."
}
  ' \
 'http://0.0.0.0:5000/'
```

- The `threshold` parameter specifies the minimal accuracy that should be considered by the classifier. Any input whose classification confidence is lower than the given threshold will not be assigned any labels.

## Upcoming features

- Output more information about the training process.
- Support classification of multiple text entries in a single request.
- Support for other classification algorithms.
