import pickle
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained-model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

# may make these more complex in the future
classes = [
    "sadness",
    "joy",
    "fear",
    "anger",
    "love",
    "surprise"
    ]

def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r'[[]]', " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]