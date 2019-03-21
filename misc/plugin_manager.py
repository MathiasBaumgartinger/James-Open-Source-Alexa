import os
import re
import importlib
import inspect

from abstract.abstract_plugin import AbstractPlugin

PATH_TO_PLUGINS = "plugins"


class PluginManager:

    def __init__(self):
        self._plugins = []

        self.load_dynamically()

    def load_dynamically(self):
        py_search_re = re.compile('.py$', re.IGNORECASE)
        plugin_files = list(filter(py_search_re.search, os.listdir(PATH_TO_PLUGINS)))
        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        plugins = list(map(form_module, plugin_files))

        modules = []
        for plugin in plugins:
            if not plugin.startswith('__'):
                modules.append(importlib.import_module(plugin, package=PATH_TO_PLUGINS))

        class_instances = []
        for module in modules:
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, AbstractPlugin):
                    class_instances.append(getattr(module, name)())

        self._plugins = class_instances

    def handle(self, command):
        score = 0
        handling_plugin = self._plugins[0]

        for plugin in self._plugins:
            if plugin.handling_score(command=command) > score:
                score = plugin.handling_score(command=command)
                handling_plugin = plugin

        handling_plugin.handle(command)
