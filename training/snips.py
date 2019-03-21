import io
import json
import os
import shutil
from os.path import isfile, join

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

DATASET_PATH = "datasets"
TRAINED_ENGINE_PATH = "nlu_trained_engine"


def train():
    """
    Opens all JSON files in DATASET_PATH, fits them to an nlu-engine, and saves the engine at TRAINED_ENGINE_PATH.

    :return: Nothing.
    """
    file_paths = [join(DATASET_PATH, file) for file in os.listdir(DATASET_PATH) if isfile(join(DATASET_PATH, file))]
    nlu_engine = SnipsNLUEngine(CONFIG_EN)

    for file_path in file_paths:
        with io.open(file_path, encoding="utf-8") as file:
            sample_dataset = json.load(file)

        nlu_engine.fit(sample_dataset)

    save_engine(nlu_engine)


def save_engine(engine):
    """
    Saves the engine at TRAINED_ENGINE_PATH, replacing an already existing engine.

    :param engine: A trained SnipsNLUEngine
    :return: Nothing.
    """
    if os.path.exists(TRAINED_ENGINE_PATH):
        shutil.rmtree(TRAINED_ENGINE_PATH)

    engine.persist(TRAINED_ENGINE_PATH)


train()
