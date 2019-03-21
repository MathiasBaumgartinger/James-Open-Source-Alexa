import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
from pathlib import Path
import os
from pocketsphinx import *


SAMPLE_DATASET_PATH = os.getcwd() + "/datasets/weather.json"
with io.open(SAMPLE_DATASET_PATH, encoding="utf-8") as f:
    sample_dataset = json.load(f)

nlu_engine = SnipsNLUEngine(CONFIG_EN)
nlu_engine.fit(sample_dataset)

nlu_engine.persist(os.getcwd() + "/nlu_trained_engine")

