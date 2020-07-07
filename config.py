import os

OUTPUT_DIR = "/app/model"

MODEL_FILE = os.getenv("MODEL_FILE", f"{OUTPUT_DIR}/model-data.bin")
DATASET_FILE = os.getenv("DATASET_FILE", "/app/dataset.csv")

API_PORT = os.getenv("API_PORT", "5000")

LANG_CODE = os.getenv("LANG_CODE", None)
