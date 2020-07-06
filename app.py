from flask import Flask, request, json
from anton.classifier import classify
from anton.cleaner import clear


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Running Text Classification API"


@app.route("/", methods=["POST"])
def hello():
    content = request.json
    text = content.get("text", "")
    threshold = content.get("threshold", .70)

    targets = classify(text, threshold)

    return json.dumps({
        "text": text,
        "threshold": threshold,
        "targets": targets,
    }), 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
