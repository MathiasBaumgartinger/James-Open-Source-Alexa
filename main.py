from pocketsphinx import *
import misc.plugin_manager as pm
from snips_nlu import SnipsNLUEngine
import json


def command():
    for phrase in LiveSpeech():
        compare = str(phrase)
        parsing = nlu_engine.parse(compare)
        print(json.dumps(parsing, indent=2))
        '''if compare == "shopping":
            print("Shopping List")
        elif compare == "spotify":
            print("Spotify")
        elif compare == 'and':
            sys.exit()
        else:
            print("Could not resolve option: ", phrase)'''
        return


plugin_manager = pm.PluginManager()
plugins = plugin_manager.load_dynamically

score = 0
handling_plugin = plugins[0]
for plugin in plugins:
        if plugin.handling_score(command="test") > score:
            score = plugin.handling_score(command="test")
            handling_plugin = plugin

model_path = get_model_path()


nlu_engine = SnipsNLUEngine.from_path("training/nlu_trained_engine")

speech = LiveSpeech(lm=False, keyphrase='james', kws_threshold=1e-20)

for keyword in speech:
    print("activated")
    command()

'''
config = {
    'verbose': False,
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}
'''
