from pocketsphinx import *
import misc.plugin_manager as pm
from snips_nlu import SnipsNLUEngine
import json

PATH_TO_NLU_ENGINE = "training/nlu_trained_engine"


def main():
    # TODO: plugin manager as static class
    plugin_manager = pm.PluginManager()

    # TODO: engine class as static class
    nlu_engine = SnipsNLUEngine.from_path("training/nlu_trained_engine")

    speech = LiveSpeech(lm=False, keyphrase='james', kws_threshold=1e-20)

    for keyword in speech:
        print("activated")
        # TODO: remove param engine because it will be static
        command(nlu_engine)


def command(nlu_engine):
    for phrase in LiveSpeech():
        compare = str(phrase)
        parsing = nlu_engine.parse(compare)
        print(json.dumps(parsing, indent=2))

        return


main()
