# data_loader.py
import json
import pandas as pd
from model_loader import MODEL

with open("shl_data.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df["embedding"] = df["Description"].apply(lambda x: MODEL.encode(x, convert_to_tensor=True))